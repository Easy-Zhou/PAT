#!/anaconda3/bin/python
# @Time    : 2019-04-18 16:24
# @Author  : zhou
# @File    : 2880
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
sql = "select * from stu where number between '1501' and '1509'"
cursor.execute(sql)
# cursor.executemany(sql,['1501','1505','1509']) 也可以
rows = cursor.fetchall()
for row in rows:
    print(row)
# connect.commit()
cursor.close()
connect.close()