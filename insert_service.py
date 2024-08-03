from apscheduler.schedulers.blocking import BlockingScheduler
import configparser
import psycopg2
import requests as rq
from requests.exceptions import RequestException, JSONDecodeError


def get_data():
    """Request to api and getting data """
    try:
        response = rq.get('http://127.0.0.1:8080/Future_settlments')
        response.raise_for_status()  # Raises an HTTPError if the response status is 4xx or 5xx
        return response.json()
    except RequestException as e:
        print(f"A network error occurred: {e}")
        return None
    except JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None


def create_conn():
    """Creates and returns a psycopg2 connection."""
    config = configparser.ConfigParser()
    path = r"C:\Users\erfan\Downloads\projects\ETL\Prediction\App\routers\DbInfo.ini"
    config.read(path)

    host = config.get('my_db', 'host')
    dbname = config.get('my_db', 'dbname')
    user = config.get('my_db', 'user')
    password = config.get('my_db', 'password')

    conn_string = f"host={host} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_string)
    return conn


def insert_data(conn):
    """Inserts data into the transactions table."""
    cur = conn.cursor()
    # query to postgres sql
    query = ('CREATE TABLE IF NOT EXISTS transactions (Amount BIGINT,date DATE,count INTEGER);'
             'INSERT INTO transactions (Amount, date, count) VALUES (%s, %s, %s);')

    inserted_data = get_data()
    try:
        cur.execute(query, inserted_data)
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def schedule_insert_job():
    """Schedules the insert job to run daily at midnight."""
    scheduler = BlockingScheduler()
    scheduler.add_job(insert_data, 'cron', hour=15, minute=30, second=0,
                      day_of_week="sat-sun-mon-tue-wed", args=[create_conn()])
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    schedule_insert_job()
