#!/anaconda3/bin/python
# @Time    : 2019-04-17 10:53
# @Author  : zhou
# @File    : conn_mysql
# @Software: PyCharm
# @Description: 

import pymysql
import configparser

config = configparser.ConfigParser()
config.read('configure.ini')
host = config['db']['host']
port = config.getint('db','port')
user = config['db']['user']
password = config['db']['password']
database = config['db']['database']
charset = config['db']['charset']


connect = pymysql.connect(host=host,
                          port=port,
                          user=user,
                          password=password,
                          database=database,
                          charset=charset)

cursor = connect.cursor()
# sql = "create table test(id int primary key,value varchar(10) not null)"
# sql = """insert into test value(1,"test")"""
# sql = "insert into stu value(%s,%s,%s,%s,%s,%s)"
#
# # sql = "select * from test"
# result = cursor.executemany(sql,[('1501','炎黄','M',78.5,70.0,100.0),
#                                  ('1505','吕萌萌','M',100.0,90.0,95.0),
#                                  ('1509','石耀举','F',60.5,90.0,70.0)])
# # rows = cursor.fetchall()
# # for row in rows:
# #     print(row)
# connect.commit()
sql = "select * from stu"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connect.close()