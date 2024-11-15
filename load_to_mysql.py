import os
import time
import pandas as pd
import sqlalchemy as db
from sqlalchemy.exc import OperationalError

# Load the CSV file
df = pd.read_csv('stock_data.csv')

# MySQL connection details from environment variables
username = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
database = os.getenv('MYSQL_DATABASE')

# Retry logic
attempt = 0
while attempt < 5:
    try:
        # Connect to MySQL
        engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
        df.to_sql('stocks', con=engine, if_exists='replace', index=False)
        print("Data loaded successfully into MySQL.")
        break
    except OperationalError:
        attempt += 1
        print(f"Attempt {attempt}: Waiting for MySQL to be ready...")
        time.sleep(5)  # Wait 5 seconds before retrying
else:
    print("Failed to connect to MySQL after several attempts.")
