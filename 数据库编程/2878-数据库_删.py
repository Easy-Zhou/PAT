#!/anaconda3/bin/python
# @Time    : 2019-04-18 16:19
# @Author  : zhou
# @File    : 2878-数据库——删
# @Software: PyCharm
# @Description:


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
sql = "delete from stu where number=%s"
cursor.executemany(sql,[('1501'),('1505'),('1509')])
# cursor.executemany(sql,['1501','1505','1509']) 也可以
connect.commit()
cursor.close()
connect.close()