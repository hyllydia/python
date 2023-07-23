# -*- coding: utf-8 -*-
# Author yhou

'''
还有几个问题， session用户登陆了的问题 , 这个问题要回顾一下cookie, session , token , flask 中session的使用
注册用户得到时候， 判断用户名是否为空的问题,
 Tips: 这两个问题都解决了
 新的问题：1、每次引用数据库都需要重新连接一遍
 2、index页面的数据需要从数据库中读取
 3、页面添加一个ip地址， 用正则取匹配ip地址， 然后将页面的数据通过ajax传递到后端去

'''

from flask import Flask,render_template,redirect,request,jsonify,url_for,session
import functools

app = Flask (__name__)
app.secret_key = "kfhglkdhg"

DATA_DICT={
    1:{'name':'judy','age':13},
    2:{'name':'jenny','age':12}

}

def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        username = session.get('xxx')
        if not username:
            return redirect(url_for('lg'))
        return func(*args,**kwargs)
    return inner

@app.route('/')
def run():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'],endpoint='lg')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('user')
    passwd = request.form.get('pwd')
    res = get_user(username,passwd)
    if res==0:
        #用户名存在并且密码正确的话 ， 直接跳转index页面
        '''session要可用的话 要依赖app.secret_key,session放在浏览器中，以前session是放在服务器中
       flask中将app.secret_key和session['xxx'] = username , 一起加密生成一个串
        flask的session通过加密的方式存储在本地浏览器的cookie中
        
        '''
        session['xxx'] = username
        print("login success!")
        return redirect(url_for('idx'))
    elif res == 1:
        # 如果密码错误的话， 还在本页面， 不需要重定向， 并且向前端传递一个错误信息显示
        error = "please input correct username/password!!"
        return render_template('login.html', error=error)
    else:
        #如果用户名不存在的话， 提示用户进行注册
        msg = "user does not exist ,please register!"
        return render_template('login.html', msg=msg)
# @app.route('/register')
# def register():
#     return

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    username = request.form.get('user')
    password = request.form.get('pwd')
    #判断用户名是否为空：为空的话报错：
    if username == "" or password == '':
        msg = "username or password can not be empty! "
        return render_template("register.html",msg=msg)
    #判断用户是否在数据库中， 在的话告知用户已经存在
    res = get_user(username,password)
    if res ==2:
        #说明用户不存在， 那么将用户名密码插入数据库中
        from condb import insert_data,query_user
        ans = insert_data(username,password)
        print(ans)
        msg = "success ,please login!"
        return render_template('register.html',msg=msg)
    else:
        #用户名已经存在
        msg = "user has been registered!"
        return render_template("register.html",msg=msg)



@app.route('/index',methods=['GET','POST'],endpoint='idx')
@auth
def index():
    if request.method == 'GET':
        data_dict = DATA_DICT
        return render_template('index.html',data_dict = data_dict)

@app.route('/edit/<int:nid>',methods=['GET','POST'])
@auth
def edit(nid):
    #前端传过来的nid是一个字符串类型， 要转换成整形
    # nid = request.args.get('nid')
    # nid = int(nid)

    if request.method == 'GET':
        info = DATA_DICT[nid]
        return render_template('edit.html',info = info)

    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    return redirect(url_for('idx'))

        #return render_template('edit.html')

@app.route('/delete/<int:nid>',methods=['GET','POST'])
@auth
def delete(nid):
    del DATA_DICT[nid]
    return redirect(url_for('idx'))
        #return render_template('edit.html')

def get_user(username,password):
    from condb import query_user
    res = query_user(username,password)
    return res
if __name__=="__main__":
    app.run(debug=True)


