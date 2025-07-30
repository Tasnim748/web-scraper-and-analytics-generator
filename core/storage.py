# storage.py

import csv
import sqlite3

def save_to_csv(data, filename):
    if not data:
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def save_to_sqlite(data, db_name, table_name="scraped_data"):
    if not data:
        return
    keys = data[0].keys()
    columns = ', '.join([f"{k} TEXT" for k in keys])
    placeholders = ', '.join(['?' for _ in keys])
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')
    c.executemany(
        f'INSERT INTO {table_name} ({", ".join(keys)}) VALUES ({placeholders})',
        [tuple(d.values()) for d in data]
    )
    conn.commit()
    conn.close()