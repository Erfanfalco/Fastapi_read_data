import configparser as cf
from sqlalchemy import create_engine
import urllib

# Read data from config
path = r"C:\Users\erfan\Downloads\projects\ETL\Prediction\App\routers\DbInfo.ini"

Config = cf.ConfigParser()
Config.read(path)

# Database credentials
username = Config.get('db_cred', 'Name')
password_encoded = urllib.parse.quote_plus(Config.get('db_cred', 'password'))
server = Config.get('db_cred', 'server')
source_name = Config.get('db_cred', 'database')

# # SQLAlchemy engine setup
engine = create_engine(
    f'mssql+pyodbc://{username}:{password_encoded}@{server}/{source_name}?driver=ODBC+Driver+17+for+SQL+Server')
