# -*- coding: utf-8 -*-
# Author WU_JUN
import pymysql

def conn():
    db = pymysql.connect(host="127.0.0.1",port=3316,user='root',password='password',db='sys',charset='utf8')
    return db
def create_table():
    db = conn()
    cur = db.cursor()
    # drop_table="drop table user_info"
    # cur.execute(drop_table)
    # create_table="CREATE TABLE user_info (id INT(10) AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255),password VARCHAR(255))"
    # cur.execute(create_table)
    data_list=[('lydia','lydia'),('jenny','jenny')]
    insert_data =  "insert into user_info(username,password) values(%s,%s)"
    cur.executemany(insert_data,data_list)
    db.commit()
    cur.close()
    db.close()

def insert_data(username,password):
    db = conn()
    cur = db.cursor()
    data_list=[(username,password)]
    print(data_list)
    insert_data = "insert into user_info(username,password) values(%s,%s)"
    cur.executemany(insert_data,data_list)
    db.commit()
    cur.close()
    db.close()
    #return "插入成功"

def query_user(username,password):
    db = conn()
    cur = db.cursor()
    cur.execute("select username,password from user_info")
    res = cur.fetchall()
    res = list(res)
    print(res)
    user_dict={}
    for item in res:
        user_dict[item[0]]=item[1]
    if username in user_dict.keys():
        if password == user_dict[username]:
            print("用户名密码正确可以登录")
            return 0
        else:
            print("密码错误")
            return 1
    else:
        print("用户名不存在，请注册!")
        return 2
    #res_id = cur.execute("select id from user_info where username=" + user1)
    #print(type(res))
    #print(res)
    #return db

#db = pymysql.connect(host="0.0.0.0",port=3316,user='root',password='password',db='UserData',charset='utf8')

if __name__ == '__main__':
    #conn()
    #create_table()
    insert_data('123','123')