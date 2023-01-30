from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from datetime import datetime
from decrypt import address, hex_to_ascii
import pandas as pd

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
exclude_keys_tx=["confirmations","n","locktime","blocktime"]

all_blocks = pd.DataFrame()
i = 0
for block_height in range(1,200000):
    i += 1
    block_hash= rpc_connection.getblockhash(block_height)
    block= rpc_connection.getblock(block_hash)
    first_tx = block['tx'][0]
    tx_coinbase= rpc_connection.getrawtransaction (first_tx, True)
    tx_dict = pd.Series([],dtype=pd.StringDtype())
    tx_dict['block_height'] = block_height
    for key, value in tx_coinbase.items():
        if key == "txid":
            tx_dict['txid'] = value
        elif key == "vin" :
            for vin_dict in value:
                for vin_key, vin_value in vin_dict.items():
                    if vin_key == "coinbase":
                        tx_dict['coinbase_hex'] = vin_value
                        tx_dict['coinbase_decoded'] = hex_to_ascii(vin_value).replace('\r', ' ').replace('\n', ' ').replace('\t', '')
        elif key == "vout" :
            all_vout = pd.DataFrame()
            for tx_cb_receiver in value:
                tx_vout = pd.Series([],dtype=pd.StringDtype())
                tx_vout['value'] = format(tx_cb_receiver['value'],'.8f')
                sc_dict = tx_cb_receiver['scriptPubKey']
                if sc_dict['type'] == 'pubkeyhash':
                    tx_vout['address']=sc_dict['address']
                elif sc_dict['type'] == 'pubkey':
                    asm_list = sc_dict['asm'].split()
                    tx_vout['address'] = address(asm_list[0], False)
                    asm_list=[]
                df_teste = tx_vout.to_frame()
                df_teste_T= df_teste.transpose()
                all_vout = pd.concat([all_vout, df_teste_T])
            all_vout.reset_index(inplace=True, drop=True)
            all_vout.rename(columns={0:"value",1:'address'},inplace=True)
            tx_dict['value'] = all_vout['value'].astype(float).sum()
            tx_dict['address'] = ', '.join(all_vout['address'])
        elif key in exclude_keys_tx:
            pass
        else:
            pass
    df = tx_dict.to_frame()
    df = pd.DataFrame.from_dict(tx_dict)   
    df_T= df.transpose()
    df_T.set_index("block_height", inplace = True)
    all_blocks = pd.concat([all_blocks, df_T])
    if i == 10:
        all_blocks["value"] = pd.to_numeric(all_blocks["value"])
        all_blocks.to_csv('All_Coinbase_Transactions_{}.csv'.format(str(datetime.today().strftime('%Y%m%d'))), escapechar='\\')
        i=0