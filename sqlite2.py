#!/usr/bin/python
# -*- coding: Shift-JIS -*-
import sqlite3

db_path = "c:\Python\SQLite\sample_data.db"
conn = sqlite3.connect(db_path)

def insert_record():
    sql = "INSERT INTO SAMPLE VALUES (1, 'あ', 'い', 'う')"
    conn.execute(sql)

    sql = "INSERT INTO SAMPLE VALUES (2, 'てすと１', 'てすと２', 'てすと３')"
    conn.execute(sql)

    sql = "INSERT INTO SAMPLE VALUES (3, '12345', '22222', '55555')"
    conn.execute(sql)

    conn.commit()
    conn.close()

insert_record()