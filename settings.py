from dotenv import load_dotenv
from os.path import join, dirname
import os
# print(os.environ.get('fec_api_key'))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

FEC_API_KEY = os.environ.get('fec_api_key')
HOST = os.environ.get('host')
DATABASE = os.environ.get('database')
USER = os.environ.get('user')
PASSWORD = os.environ.get('password')


print(HOST)
print(DATABASE)
print(USER)
print(PASSWORD)