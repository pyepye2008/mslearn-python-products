#学习Flask 2024年02月25日 Stanley

from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hello(name):
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
          return redirect(url_for('hello',name='post success'))
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

if __name__ == '__main__':
   #app.run(host, port, debug, options) 
   #host = '0.0.0.0' 代表外网访问，127.0.0.1 代表本机访问
   app.run(host='0.0.0.0',debug=True,port=6001)
   #app.run()

