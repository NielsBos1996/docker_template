from mysql.connector import connect, Error
import time

def executeQuery(query: str):
    try:
        with connect(
            host='mysql-database', # all these values are defined in docker-compose
            user='root',
            password='',
            database='db',
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
    except Exception as e:
        print(f'error while executing query {query}')
        raise e

def createTable():
    time.sleep(5)  # mySQL is slower to start than python
    executeQuery('''
        create table if not exists clicks(
            id int(32) NOT NULL PRIMARY KEY AUTO_INCREMENT,
            time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            user varchar(30) NOT NULL
        )
    ''')
    print('table created successfully')
