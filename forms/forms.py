#动态表单 WTF Stanley 2024年09月12日
from flask_wtf import FlaskForm
from wtforms import Form, HiddenField, StringField,IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators

class ContactForm(Form):
   hidden_tag = HiddenField()
   name = StringField("Name Of Student",[validators.DataRequired("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')] )
   Address = TextAreaField("Address",[validators.DataRequired("Please enter your address.")])
   email = StringField("Email",[validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
   Age = IntegerField("age",[validators.DataRequired("Please enter afge.")])
   language = SelectField('Languages', choices = [('cpp', 'C++'),   ('py', 'Python')])
   submit = SubmitField("Send")
