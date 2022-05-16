#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

db_path = "C:\Python\SQLite\jvn.db"
conn = sqlite3.connect(db_path)

def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS SAMPLE
                 (JVNCODE   TEXT PRIMARY KEY,
                  DATE TEXT,
                  URL TEXT)'''

    conn.execute(sql)
    conn.commit()
    conn.close()

create_table()

# DBÇ∆ÇÃê⁄ë±Çï¬Ç∂ÇÈ(ïKê{)
conn.close()