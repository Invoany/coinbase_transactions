from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pprint import pprint
import logging
from config import rpcuser, rpcpassword, host, port, timeout
#~/umbrel/scripts/app restart bitcoin
#logging.basicConfig()
#logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)
from sql_test import bitcoin_sqlite3, check_database, check_max
#rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpcuser, rpcpassword), timeout=120)

#block_count = rpc_connection.getblockcount()
print("---------------------------------------------------------------")
#print("Block Count:", block_count)
print("---------------------------------------------------------------")
#block_count = rpc_connection.getblock('0059a1dc8d4eba60af60675e6c25fc08e5bdd4a4d81858f092fbf06c8bf7b009')
print("---------------------------------------------------------------")
#print("Block Count:", block_count)
print("---------------------------------------------------------------")

print(check_max())