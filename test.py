from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from datetime import datetime
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
blockchain_info = rpc_connection.getblockchaininfo()

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
        print(key.title() +" - " + str(value))

print("----------------")
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
tx_coinbase= rpc_connection.getrawtransaction ("c13e29f092b13cf77f63c26f6adacb149b123c590e4a391625c1fc527d7ed400", True)
#tx_coinbase= rpc_connection.getrawtransaction ("10b54fd708ab2e5703979b4ba27ca0339882abc2062e77fbe51e625203a49642", True)
#tx_coinbase= rpc_connection.getrawtransaction ("02f754075a7fae665fa4440b799c711e319a56357eda6e6bc84d40220b200361", False)
print(tx_coinbase)

print("----------------")
for block_height in range(1,2):
    block_hash= rpc_connection.getblockhash(block_height)
    block= rpc_connection.getblock(block_hash)
    first_tx = block['tx'][0]
    tx_coinbase= rpc_connection.getrawtransaction (first_tx, True)
    print(tx_coinbase)
    tx_decode_coinbase= rpc_connection.decoderawtransaction(tx_coinbase)
    
    print("One")
    create_wallet = rpc_connection.createwallet("teste")
    tx_gettransaction_coinbase= rpc_connection.gettransaction(tx_coinbase, True,False)
    print(tx_decode_coinbase)
