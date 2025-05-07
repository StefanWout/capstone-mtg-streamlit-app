import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from env.dev
load_dotenv(dotenv_path="c:/Users/stefa/Documents/Digital Futures/capstone-mtg-streamlit-app/env.dev")

# Retrieve database connection details from environment variables
DB_NAME = os.getenv("TARGET_DB_NAME")
DB_USER = os.getenv("TARGET_DB_USER")
DB_PASSWORD = os.getenv("TARGET_DB_PASSWORD")
DB_HOST = os.getenv("TARGET_DB_HOST")
DB_PORT = os.getenv("TARGET_DB_PORT")

# Create a connection string
connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Test the connection
try:
    engine = create_engine(connection_string)
    connection = engine.connect()
    print(f"Successfully connected to the database: {DB_NAME}")
    connection.close()
except Exception as e:
    print(f"Failed to connect to the database: {e}")
    
    
print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PASSWORD: {DB_PASSWORD}")
print(f"DB_HOST: {DB_HOST}")
print(f"DB_PORT: {DB_PORT}")