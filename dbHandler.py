import configeration
#import mysql
import sqlite3
from cryptography.fernet import Fernet
from collections import Counter

#Globals
cipherSuite = Fernet(configeration.key)

#TODO: Integrate with remote database. Stored procedures to be used in mysql for fetch and update.

def getDB():
    '''
        Connect to database based on config and return db connection
    '''
    #dbConnection = mysql.connector.connect(
    #  host=configeration.host,
    #  user=configeration.user,
    #  passwd=bytes(cipherSuite.decrypt(configeration.password)).decode("utf-8"),
    #  database=configeration.db
    #)
    #return dbConnection.cursor()
    dbConnection = sqlite3.connect(':memory:')
    dbConnection.row_factory = sqlite3.Row
    return dbConnection

def fetchData(db, topX=None ):
    '''
        Fetch data from table words. topX returns the top X rows.
        Note: db has to be passed around due to in meomory database.
    '''
    cursor = db.cursor()
    if topX:
        data=cursor.execute(''' SELECT word, frequncy FROM words ORDER BY frequncy DESC LIMIT ? ''',(topX,))
    else:
        data=cursor.execute(''' SELECT word, frequncy FROM words ORDER BY frequncy DESC ''')
    return data.fetchall()

def fetchDB():
    '''
        Create and initialise a databse for running application
        Note: db has to be passed around due to in meomory database.
    '''
    db=getDB()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE words (hash TEXT PRIMARY KEY, word TEXT, frequncy INTEGER) ''')
    db.commit()
    return db

def updateWords(db, listWords ):
    '''
        Create and initialise a databse for running application.
        Note: db has to be passed around due to in meomory database.
    '''
    cursor = db.cursor()
    oldWords=fetchData(db)
    allwords=Counter(oldWords) + Counter(listWords)
    placeholders=[[cipherSuite.encrypt(str(k).encode('ascii')).decode("utf-8"),k,v] for k,v in allwords.items()]
    cursor.executemany(''' INSERT INTO users(hash, word, frequncy VALUES(?,?,?)''', placeholders.values())
    db.commit()
    return allwords
