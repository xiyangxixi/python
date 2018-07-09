#! /usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector
db_host = '192.168.29.251'
db_user = 'root'
db_password = '123456'
db_port = '3306'
db_database = 'test'
conn = mysql.connector.connect(host = db_host, user = db_user, password = db_password, port = db_port, database = db_database)
cursor = conn.cursor()
cursor.execute('select * from test')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
