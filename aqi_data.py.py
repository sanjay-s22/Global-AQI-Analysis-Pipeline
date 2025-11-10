import pandas as pd
from sqlalchemy import create_engine, text
import mysql.connector

# --- Configuration ---
DB_NAME = 'aqi_project'
DB_USER = 'root'
DB_PASS = 'root' # Update this to your MySQL password
DB_HOST = 'localhost'
CSV_FILE = 'global_aqi_project_data.csv'
TABLE_NAME = 'global_aqi'

# --- 1. Database Connection and Creation ---
try:
    # Connect to the MySQL server
    engine_base = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}')
    
    with engine_base.connect() as connection:
        print(f"Checking for database: {DB_NAME}")
        result = connection.execute(text(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{DB_NAME}'"))
        
        if result.fetchone() is None:
            connection.execute(text(f"CREATE DATABASE {DB_NAME}"))
            print(f"Database '{DB_NAME}' created successfully.")
        else:
            print(f"Database '{DB_NAME}' already exists.")
            
        connection.commit()

except Exception as e:
    print(f"Error during initial database connection/creation: {e}")
    exit()

# --- 2. Data Loading and Cleaning ---
try:
    # Connect to the target database
    engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
    
    print(f"\nLoading data from {CSV_FILE}...")
    df = pd.read_csv(CSV_FILE)
    
    # Clean column names
    df.columns = df.columns.str.replace(' ', '_')

    # --- 3. Write DataFrame to MySQL ---
    print(f"Uploading data to table: {TABLE_NAME}")
    df.to_sql(name=TABLE_NAME, con=engine, if_exists='replace', index=False, chunksize=10000)
    print("Data upload complete!")
    
    # --- 4. Verification ---
    with engine.connect() as connection:
        count_query = f"SELECT COUNT(*) FROM {TABLE_NAME}"
        count_result = connection.execute(text(count_query)).scalar()
        print(f"Verification: {count_result} rows loaded into {TABLE_NAME}.")

except FileNotFoundError:
    print(f"Error: The file '{CSV_FILE}' was not found. Make sure it's in the same directory.")
except Exception as e:
    print(f"Error during data loading or connection: {e}")