from sqlalchemy import create_engine
from configparser import ConfigParser, RawConfigParser
import os
import platform
from settings import HOST, DATABASE, USER, PASSWORD


def get_postgres_config():
    if HOST:
        user = USER
        password = PASSWORD
        host = HOST
        database = DATABASE
        engine_string = f"""postgresql+psycopg2://{user}:{password}@{host}/{database}"""
        # engine_string = get_postgres_settings()
        db_engine = create_engine(engine_string, isolation_level="AUTOCOMMIT")
    else:
        raise Exception('no HOST setting found.  Is your .env setup yet?')        
    return db_engine


if __name__ == "__main__":
    print(get_postgres_config())


