import pandas as pd
import sqlite3

# 1 Load Data from csv and json files
orders = pd.read_csv('orders.csv')
users = pd.read_json('users.json')

# SQL File read 
conn = sqlite3.connect(':memory:')
with open('restaurants.sql', 'r') as f:
    conn.executescript(f.read())
restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)
conn.close()

# 2 Merge (Joining Tables) left join done for both

temp_df = pd.merge(orders, users, on='user_id', how='left')

# Ab results ko restaurants ke sath jodein 'restaurant_id' ke basis par
final_df = pd.merge(temp_df, restaurants, on='restaurant_id', how='left')

# 3. Final CSV Done.
final_df.to_csv('final_food_delivery_dataset.csv', index=False)

print("Done it ready csv file.")