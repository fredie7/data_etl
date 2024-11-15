import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import os

# Define the PostgreSQL connection URL (make sure this is correctly set in your Docker environment)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/postgresdb")

# Set up the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Example function to load the DataFrame into PostgreSQL
def load_to_postgres(df):
    try:
        # Insert the data into the PostgreSQL database
        # 'stocks_data' is the name of the table in PostgreSQL
        # if_exists='replace' will replace the table if it already exists, use 'append' if you want to add data
        df.to_sql('uk_stocks_data', engine, index=False, if_exists='replace')
        print("Data loaded successfully to PostgreSQL")
    except OperationalError as e:
        print(f"OperationalError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Load your stock data (make sure the file path is correct)
    # Ensure that the file is located correctly in the Docker container or mount a volume to access it.
    try:
        stock_df = pd.read_csv('/app/uk_stock_data.csv')  # Update path if necessary
        print("CSV loaded successfully.")
        
        # Load the dataframe to PostgreSQL
        load_to_postgres(stock_df)
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
