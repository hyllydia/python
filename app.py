# -*- coding: utf-8 -*-
# Author yhou

from flask import Flask,render_template,redirect,request,jsonify,url_for

app = Flask (__name__)

DATA_DICT={
    1:{'name':'judy','age':13},
    2:{'name':'jenny','age':12}

}
@app.route('/login',methods=['GET','POST'],endpoint='lg')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('user')
    passwd = request.form.get('pwd')
    if username == 'lydia' and passwd == 'lydia':
        return redirect('/index')
    #如果用户名密码错误的话， 还在本页面， 不需要重定向， 并且向前端传递一个错误信息显示
    error = "please input correct username/password!!"
    #return "login error"
    return render_template('login.html',error=error)

@app.route('/index',methods=['GET','POST'],endpoint='idx')
def index():
    if request.method == 'GET':
        data_dict = DATA_DICT
        return render_template('index.html',data_dict = data_dict)

@app.route('/edit/<int:nid>',methods=['GET','POST'])
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
def delete(nid):
    del DATA_DICT[nid]
    return redirect(url_for('idx'))
        #return render_template('edit.html')

if __name__=="__main__":
    app.run(debug=True)


