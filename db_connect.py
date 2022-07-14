from sqlalchemy import create_engine
from configparser import ConfigParser, RawConfigParser
import os
import platform

import sqlalchemy
from settings import HOST, DATABASE, USER, PASSWORD


def get_postgres_config():
    if HOST:
        user = USER
        password = PASSWORD
        host = HOST
        database = DATABASE        
        engine_string = f"""postgresql+psycopg2://{user}:{password}@{host}/{database}"""
        # engine_string = get_postgres_settings()
        # print(engine_string)
        db_engine = create_engine(engine_string, isolation_level="AUTOCOMMIT")
    else:
        raise Exception('no HOST setting found.  Is your .env setup yet?')        
    return db_engine


def get_postgres_default_config():
    if HOST:
        user = USER
        password = PASSWORD
        host = HOST
        database = "postgres"     
        engine_string = f"""postgresql+psycopg2://{user}:{password}@{host}/{database}"""
        # engine_string = get_postgres_settings()
        print(engine_string)
        db_engine = create_engine(engine_string, isolation_level="AUTOCOMMIT")
    else:
        raise Exception('no HOST setting found.  Is your .env setup yet?')        
    return db_engine


def generic_default_sql(sql):
    sql = sqlalchemy.text(sql)
    # engine = get_postgres_config()
    engine = get_postgres_default_config()
    conn = None
    conn = engine.connect()
    conn.autocommit = True
    try:
        conn.execute(sql)
    except Exception as e:
        raise
    conn.close()
    
    

def generic_sql(sql):
    sql = sqlalchemy.text(sql)
    engine = get_postgres_config()
    # engine = get_postgres_default_config()
    conn = None
    conn = engine.connect()
    conn.autocommit = True
    try:
        conn.execute(sql)
    except Exception as e:
        raise
    conn.close()    

if __name__ == "__main__":
    generic_default_sql("CREATE DATABASE fec;")
    # print(HOST)
    # print(DATABASE)
    # print(USER)
    # print(PASSWORD)
    # print(get_postgres_config())


