#学习Flask 2024年02月25日 Stanley

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
   #app.run(host, port, debug, options) 
   #host = '0.0.0.0' 代表外网访问，127.0.0.1 代表本机访问
   app.run(host='0.0.0.0',debug=True,port=6001)
   #app.run()
   