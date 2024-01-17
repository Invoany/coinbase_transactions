import time
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from Config.config import rpcuser, rpcpassword, host, port, timeout, seconds

seconds=40

# This Function returns the Hash of a given block height
def getblockhash(block_height):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        block_hash= rpc_connection.getblockhash(block_height)
    except:
        print("Got error waiting",seconds , "seconds on getblockhash")
        time.sleep(seconds)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        block_hash= rpc_connection.getblockhash(block_height)
    return block_hash

# This funtion returns information from a given block hash, like all transactions inside, time, difficulty, etc
def getblock(block_hash):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        block= rpc_connection.getblock(block_hash)
    except:
        print("Got error waiting",seconds , "seconds on getblock")
        time.sleep(seconds)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        block= rpc_connection.getblock(block_hash)
    return block

# Returns all data of a specific transaction
def getrawtransaction(tx):
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        tx= rpc_connection.getrawtransaction(tx, True)
    except:
        print("Got error waiting",seconds , "seconds on getrawtransaction")
        time.sleep(seconds)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        tx= rpc_connection.getrawtransaction(tx, True)
    return tx

# Retirve total count of blocks in Blockchain
def getblockcount():
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
    try:
        block_height= rpc_connection.getblockcount()
    except:
        print("Got error waiting",seconds , "seconds on getblockcount")
        time.sleep(seconds)
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpcuser, rpcpassword, host, port ), timeout=timeout)
        block_height= rpc_connection.getblockcount()
    return block_height

if __name__ == "__main__":
    #print(getblockhash(350000))
    #print(getblock("0000000000000000053cf64f0400bb38e0c4b3872c38795ddde27acb40a112bb"))
    print(getblockcount())
    #pass