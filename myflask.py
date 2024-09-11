#学习Flask 2024年02月25日 Stanley

from flask import Flask, flash, make_response, redirect, render_template, request, session, url_for
app = Flask(__name__)
app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj' #设定 Session时需要一个秘钥

@app.route('/')
def index():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name):
    if 'username' in session:
       username = session['username']
       return 'Logged in as ' + username + '<br>'      "<b><a href = '/logout'>click here to log out</a></b>"
    
    return 'Hello, %s! <br/> <a href=/login>Back</a> ' % name   

#动态跳转
@app.route('/user/<username>')
def show_user_profile(username):
    
    if username == 'admin':
       return redirect(url_for('hello',name='admin'))
    else:
       return redirect(url_for('hello', name="guest"))   
    
#渲染Html,表单
@app.route('/login', methods=['GET', 'POST'])
def login():    
    
    if request.method == 'POST':
       print("use post")
       nm = request.form['nm']   
       if nm == 'admin':
          #存储session
          session['username'] = nm
          #闪现消息
          flash('You were successfully logged in')
          return redirect(url_for('index',name='post success'))
       else:
          return redirect(url_for('hello', name= 'post fail'))   
    else: 
       
       if request.method == 'GET':
          print("use get")
          nm = request.args.get('nm')
          #判断两边是否空值，strip()去除两边空格或指定字符
          if nm is not None and nm.strip() != '' :
            if nm == 'admin':
               return redirect(url_for('hello',name='get success'))
            else:
               return redirect(url_for('hello', name= 'get fail'))   
          else:
             return render_template('login.html')  
       else:  
          return render_template('login.html')        

#退出登录
@app.route('/logout')
def  logout():
    session.pop('username', None)
    return redirect(url_for('login'))

#渲染更多内容,传入不同类型的参数
@app.route('/info')
def info():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    
    return render_template('info/info.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                          )

#页面结果传递
@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html', result=result)

#Cookier的设定
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    #设定响应
    resp = make_response("set success") 
    resp = make_response('Custom Response')
    resp.headers['X-Custom-Header'] = 'Some value header info'
    resp.status_code = 201
    
    resp.set_cookie("mycookie", "pyepye",max_age=3600)
    return resp   
 
 #读取Cookier
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('mycookie')
    return name
 
#删除Cookier
@app.route('/delcookie')
def delcookie():
    resp = make_response("del success")
    resp.delete_cookie("mycookie")
    return resp

if __name__ == '__main__':
   #app.run(host, port, debug, options) 
   #host = '0.0.0.0' 代表外网访问，127.0.0.1 代表本机访问
   app.run(host='0.0.0.0',debug=True,port=6001)
   #app.run()

