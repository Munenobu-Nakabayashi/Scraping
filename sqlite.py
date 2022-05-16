#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

db_path = "C:\Python\SQLite\jvn.db"
conn = sqlite3.connect(db_path)

def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS JVN
                 (JVNCODE    TEXT PRIMARY KEY,
                  JVNDATE TEXT,
                  JVNURL TEXT)'''

    conn.execute(sql)
    conn.commit()
    conn.close()

create_table()

# DBÇ∆ÇÃê⁄ë±Çï¬Ç∂ÇÈ(ïKê{)
conn.close()