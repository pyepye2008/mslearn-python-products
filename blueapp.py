from flask import Flask

app = Flask(__name__)

# 导入蓝图
from auth.routes import auth
from blog.routes import blog

# 注册蓝图
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(blog, url_prefix='/blog')

if __name__ == '__main__':
   #app.run(host, port, debug, options) 
   #host = '0.0.0.0' 代表外网访问，127.0.0.1 代表本机访问
   app.run(host='0.0.0.0',debug=True,port=6001)
   #app.run()