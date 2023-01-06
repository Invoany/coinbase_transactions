from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
num_blocks_hash = rpc_connection.getbestblockhash()
num_blocks = rpc_connection.getblockcount()
blockchain_info = rpc_connection.getblockchaininfo()
print("Hash of the best block - " + num_blocks_hash)
print("Last Block - " + str(num_blocks))
print(blockchain_info)
print("----------")
print(blockchain_info.keys())

for key, value in blockchain_info:
    print(key)
    print(value)