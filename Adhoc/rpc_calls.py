import time
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from Config.config import rpcuser, rpcpassword, host, port, timeout

def getblockhash(block_height):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        block_hash= rpc_connection.getblockhash(block_height)
    except:
        print("Got error waiting 60 seconds on getblockhash")
        time.sleep(60)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        block_hash= rpc_connection.getblockhash(block_height)
    return block_hash

def getblock(block_hash):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        block= rpc_connection.getblock(block_hash)
    except:
        print("Got error waiting 60 seconds on getblock")
        time.sleep(60)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        block= rpc_connection.getblock(block_hash)
    return block

def getrawtransaction(first_tx):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        tx= rpc_connection.getrawtransaction(first_tx, True)
    except:
        print("Got error waiting 60 seconds on getrawtransaction")
        time.sleep(60)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        tx= rpc_connection.getrawtransaction(first_tx, True)
    return tx

if __name__ == "__main__":
    print(getblockhash(350000))
    print(getblock("0000000000000000053cf64f0400bb38e0c4b3872c38795ddde27acb40a112bb"))
    pass