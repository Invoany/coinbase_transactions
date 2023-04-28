import sqlite3
import shutil

#Receive a dataframe
def bitcoin_sqlite3(df,insert_type):
    connection = sqlite3.connect("coinbase_tansactions.db")
    cursor = connection.cursor()
    df.to_sql('bitcoin_coinbase_tx', connection, if_exists = insert_type, index=True)
    connection.commit()

def check_database():
    connection = sqlite3.connect("coinbase_tansactions.db")
    cursor = connection.cursor()
    for row in cursor.execute("select * from bitcoin_coinbase_tx"):
        print(row)
    connection.commit()
    
def check_max():
    connection = sqlite3.connect("coinbase_tansactions.db")
    cursor = connection.cursor()
    for value in cursor.execute("select MAX(block_height) from bitcoin_coinbase_tx"):
        max_block_height = value[0]
    connection.commit()
    return max_block_height