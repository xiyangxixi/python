#! /usr/bin/env python
# -*- coding: utf-8 -*-

import  mysql.connector
conn = mysql.connector.connect(host='192.168.29.251', user='root', password='123456', port='3306', database='test')
cursor = conn.cursor()
#cursor.execute('create table user (id  varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'huahua'])
#count = cursor.rowcount
#print(count)
#conn.commit()
#cursor.close()
cursor = conn.cursor()
cursor.execute('select count(1) from user')
total = cursor.fetchall()
print(total)
cursor.close()
conn.close