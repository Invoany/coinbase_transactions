from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
#from datetime import datetime
from decrypt import address, hex_to_ascii

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
"""blockchain_info = rpc_connection.getblockchaininfo()

exclude_keys=["softforks","automatic_pruning","prune_target_size","pruneheight","initialblockdownload", "pruned"]
for key, value in blockchain_info.items():
    if key == "size_on_disk":
        print(key.title() +" - " + str(round(value/1024/1024/1024,2)) + " Gb")
    elif key == "time":
        print(key.title() +" - " + str(datetime.fromtimestamp( value )))
    elif key == "mediantime":
        print(key.title() +" - " + str(datetime.fromtimestamp( value )))
    elif key in exclude_keys:
        pass
    else:
        print(key.title() +" - " + str(value))"""

"""rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
tx_coinbase= rpc_connection.getrawtransaction ("c13e29f092b13cf77f63c26f6adacb149b123c590e4a391625c1fc527d7ed400", True)
#tx_coinbase= rpc_connection.getrawtransaction ("10b54fd708ab2e5703979b4ba27ca0339882abc2062e77fbe51e625203a49642", True)
#tx_coinbase= rpc_connection.getrawtransaction ("02f754075a7fae665fa4440b799c711e319a56357eda6e6bc84d40220b200361", False)
print(tx_coinbase)"""

#print("----------------")
exclude_keys_tx=["confirmations","n","locktime","blocktime"]
for block_height in range(0,10):
    block_hash= rpc_connection.getblockhash(block_height)
    block= rpc_connection.getblock(block_hash)
    first_tx = block['tx'][0]
    tx_coinbase= rpc_connection.getrawtransaction (first_tx, True)
    #print(tx_coinbase)
    #tx_decode_coinbase= rpc_connection.decoderawtransaction(tx_coinbase)
    #print("---------")
    print(str("block height") + " - " + str(block_height))
    for key, value in tx_coinbase.items():
        if key == "txid":
            print(str(key) + " - " + str(value))
        elif key == "vin" :
            for vin_dict in value:
                for vin_key, vin_value in vin_dict.items():
                    if vin_key == "coinbase":
                        print(str(vin_key) + " - " + str(vin_value))
                        print("The decoded Conbase - " + hex_to_ascii(vin_value))
        elif key == "vout" :
            for vin_dict in value:
                for vin_key, vin_value in vin_dict.items():
                    if vin_key == "scriptPubKey":
                        for pub_key, pub_value in vin_value.items():
                            if pub_key == "type":
                                print(str(pub_key) + " - " + str(pub_value))
                            elif pub_key == "asm":
                                asm_list = pub_value.split()
                                print("address - " + str(address(asm_list[0], False)))
                    else:
                        pass
                        #print(str(vin_key) + " - " + str(vin_value))
        elif key in exclude_keys_tx:
            pass
        else:
            pass
            #print(str(key) + " - " + str(value))            