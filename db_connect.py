from sqlalchemy import create_engine
from configparser import ConfigParser, RawConfigParser
import os
import platform


def config_postgres(section='postgresql'):
    # print(platform.system())
    if platform.system() == 'Linux':
        filename = f"{os.getcwd()}/db_config.ini"
    else:
        filename='C:\\Users\\timko\\code\\fcc_django\\fcc\\model_loader\\db_config.ini'
    
    # create a parser
    parser = ConfigParser()
    # read config file\\
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            if param[0] == 'user':
                user = param[1]
            if param[0] == 'password':
                password = param[1]
            if param[0] == 'host':
                host = param[1]
            if param[0] == 'database':                                              
                database = param[1]
        db = f"""postgresql+psycopg2://{user}:{password}@{host}/{database}"""
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db  


def get_postgres_config():
    engine_string = config_postgres()
    db_engine = create_engine(engine_string, isolation_level="AUTOCOMMIT")
    return db_engine


if __name__ == "__main__":
    # pass
    print(os.getcwd())
    print(platform.system())


