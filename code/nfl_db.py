import os
import pandas as pd
import sqlite3

# Create empty database.
conn = sqlite3.connect('nfl.db')

# Bring in NFL data.
df = pd.read_csv('../data/nfl.csv')

# Create table out of NFL dataframe, if it doesn't already exist.
try:
    df.to_sql(name='nfl', con=conn, index=False)
except ValueError:
    print('Error: NFL table already exists')
finally:
    conn.close()