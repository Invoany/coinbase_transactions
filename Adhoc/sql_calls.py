import sqlite3

#Receive a dataframe df for Insertion, and a string "append" or "replace"
def bitcoin_sqlite3(df,insert_type):
    connection = sqlite3.connect("coinbase_txs.db")
    cursor = connection.cursor()
    df.to_sql('bitcoin_coinbase_tx', connection, if_exists = insert_type, index=True)
    connection.commit()

# Prints all lines of the database
def check_database():
    connection = sqlite3.connect("coinbase_txs.db")
    cursor = connection.cursor()
    for row in cursor.execute("select * from bitcoin_coinbase_tx"):
        print(row)
    connection.commit()
# Return Max block_height of Database
def check_max():
    connection = sqlite3.connect("coinbase_txs.db")
    cursor = connection.cursor()
    for value in cursor.execute("select MAX(block_height) from bitcoin_coinbase_tx"):
        max_block_height = value[0]
    connection.commit()
    return max_block_height

if __name__ == "__main__":
    #print(check_max())
    pass