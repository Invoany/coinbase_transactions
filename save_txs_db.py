import pandas as pd
from Adhoc.sql_calls import bitcoin_sqlite3, check_database, check_max
from Adhoc.rpc_calls import getblockhash, getblock, getrawtransaction, getblockcount
from Adhoc.decrypt import address, hex_to_ascii

try:
    min_height = check_max() + 1
    insert_type = 'append'
except:
    min_height = 1
    insert_type = 'replace'

max_height = getblockcount()
all_blocks = pd.DataFrame()
i = 0

for block_height in range(min_height,max_height):
    i += 1
    coinbase_txid = getblock(getblockhash(block_height))['tx'][0]
    tx_coinbase= getrawtransaction(coinbase_txid)
    series_tx = pd.Series([],dtype=pd.StringDtype())
    series_tx['block_height'] = block_height
    series_tx['txid'] = coinbase_txid
    for key, value in tx_coinbase.items():
        if key == "vin" :
            for vin_dict in value:
                for vin_key, vin_value in vin_dict.items():
                    if vin_key == "coinbase":
                        series_tx['coinbase_hex'] = vin_value
                        series_tx['coinbase_decoded'] = hex_to_ascii(vin_value)
        elif key == "vout":
            a_value = []
            b_value = []
            for tx_cb_receiver in value:
                a_value.append(format(tx_cb_receiver['value'],'.8f'))
                sc_dict = tx_cb_receiver['scriptPubKey']
                if sc_dict['type'] == 'pubkeyhash':
                    b_value.append(sc_dict['address'])
                elif sc_dict['type'] == 'nonstandard':
                    b_value.append("nonstandard")
                elif sc_dict['type'] == 'pubkey':
                    asm_list = sc_dict['asm'].split()
                    b_value.append(address(asm_list[0], False))
            series_tx['value'] = sum(list(map(float,a_value)))
            series_tx['address'] = ','.join(b_value)
    df = series_tx.to_frame()   
    df_T= df.transpose()
    df_T.set_index("block_height", inplace = True)
    all_blocks = pd.concat([all_blocks, df_T])
    if i==100 or block_height == (max_height - 1):
        bitcoin_sqlite3(all_blocks,insert_type)
        all_blocks = pd.DataFrame() 
        i=0