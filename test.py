from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
blockchain_info = rpc_connection.getblockchaininfo()

exclude_keys=["softforks","automatic_pruning","prune_target_size","pruneheight","initialblockdownload"]
for key, value in blockchain_info.items():
    if key == "size_on_disk":
        print(key.title() +" - " + str(round(value/1024/1024/1024,2)) + " Gb")
    elif key in exclude_keys:
        pass
    else:
        print(key.title() +" - " + str(value))