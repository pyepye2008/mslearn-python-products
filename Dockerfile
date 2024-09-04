#WORKDIR/ opt/Langyang/orange
#MD python manage.py server --debug
FROM python:3.12.5
LABEL maintainer="py312"
RUN mkdir /myapp

# 创建 app 目录
WORKDIR /myapp
# 安装 app 依赖
COPY requirements.txt ./
RUN pip install -r requirements.txt
#打包 app 源码
COPY /data/* /myapp/data/
COPY /templates/* /myapp/templates/
COPY /app.py /myapp/
EXPOSE 5000

CMD [ "python","app.py" ]