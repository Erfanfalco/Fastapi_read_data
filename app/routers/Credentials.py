import configparser as cf
from sqlalchemy import create_engine
import urllib


# Read data from config
path = r"C:\Users\erfan\Downloads\projects\ETL\Prediction\App\routers\DbInfo.ini"

Config = cf.ConfigParser()
Config.read(path)


# sql Database credentials
username = Config.get('db_cred', 'Name')
password_encoded = urllib.parse.quote_plus(Config.get('db_cred', 'password'))
server = Config.get('db_cred', 'server')
source_name = Config.get('db_cred', 'database')


# SQLAlchemy engine setup
sql_engine = create_engine(
    f'mssql+pyodbc://{username}:{password_encoded}@{server}/{source_name}?driver=ODBC+Driver+17+for+SQL+Server')


# Postgres Database credentials
p_username = Config.get('my_db', 'user')
p_password_encoded = urllib.parse.quote_plus(Config.get('my_db', 'password'))
p_server = Config.get('my_db', 'host')
p_source_name = Config.get('my_db', 'dbname')

postgres_path = 'postgresql+psycopg2://' + p_username + ':' + p_password_encoded + '@' + p_server + '/' + p_source_name

# SQLAlchemy engine setup
postgres_engine = create_engine(postgres_path)


