from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.before_app_request
def before_request():
    # 执行在每个请求之前的操作
    pass

@auth.after_app_request
def after_request(response):
    # 执行在每个请求之后的操作
    return response