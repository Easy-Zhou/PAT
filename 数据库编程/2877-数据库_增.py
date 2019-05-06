#!/anaconda3/bin/python
# @Time    : 2019-04-18 16:17
# @Author  : zhou
# @File    : 2877-数据库_增
# @Software: PyCharm
# @Description: 

import pymysql
import configparser

config = configparser.ConfigParser()
config.read('configure.ini')
host = config['db']['host']
port = config.getint('db', 'port')
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
sql = "insert into student value(%s,%s,%s,%s,%s,%s)"

result = cursor.executemany(sql, [('1601', '炎黄', 'M', 78.5, 70.0, 100.0),
                                  ('1605', '吕萌萌', 'M', 100.0, 90.0, 95.0),
                                  ('1609', '石耀举', 'F', 60.5, 90.0, 70.0),
                                  ('1701', '炎黄', 'M', 78.5, 70.0, 100.0),
                                  ('1705', '吕萌萌', 'M', 100.0, 90.0, 95.0),
                                  ('1709', '石耀举', 'F', 60.5, 90.0, 70.0),
                                  ('1801', '炎黄', 'M', 78.5, 70.0, 100.0),
                                  ('1805', '吕萌萌', 'M', 100.0, 90.0, 95.0),
                                  ('1809', '石耀举', 'F', 60.5, 90.0, 70.0),
                                  ('1901', '炎黄', 'M', 78.5, 70.0, 100.0),
                                  ('1905', '吕萌萌', 'M', 100.0, 90.0, 95.0),
                                  ('1909', '石耀举', 'F', 60.5, 90.0, 70.0)])

connect.commit()
cursor.close()
connect.close()
