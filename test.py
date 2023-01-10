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
tx_coinbase= rpc_connection.getrawtransaction ("bbd5dabf72330f2b6342dd879628c144c702abbdca2443d37c43d422a1c2d831", True)
#tx_coinbase= rpc_connection.getrawtransaction ("4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b", True)
print(tx_coinbase)


print("----------------")
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%("umbrel", "MUwukWorrYkL75vkfZ6NMmM_lxGFw7h1hGTPIlDbJl8="))
tx_decode_coinbase= rpc_connection.decoderawtransaction("010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff6403135d0a544e5954696d65732031302f4d61722f3230323120486f7573652047697665732046696e616c20417070726f76616c20746f20426964656e27732024312e39542050616e64656d69632052656c6965662042696c6c104d696e650500823537606671160004e352352d000000001976a914c825a1ecf2a6830c4401620c3a16f1995057c2ab88ac0000000000000000266a24aa21a9ed56fbd7c20728cca282101503294bdebfea5395acd9da5defdac84eaf5f00f6da00000000000000002c6a4c2952534b424c4f434b3a7ca43fda075fd6c14116426d4af0f9046eba4fd5827012aaac2e40250031d67a0000000000000000266a24b9e11b6d265b84a9a0bbaf710eee225a8abd434a0fea9cf06e6ca2f56a77e33f30872c5a01200000000000000000000000000000000000000000000000000000000000000000a19acd48")
print(tx_decode_coinbase)