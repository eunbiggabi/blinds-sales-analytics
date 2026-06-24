import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="blinds_db",
    user="postgres",
    password="YOUR_PASSWORD"
)

cur = conn.cursor()

print("Connected successfully!")