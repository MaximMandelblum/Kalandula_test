from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, HiddenField
from wtforms.validators import DataRequired


class GetEC2Instances(FlaskForm):
    region = SelectField('region', choices=[])
    submit = SubmitField('get servers')


class WriteLog(FlaskForm):
    level = SelectField('log level', choices=[])
    submit = SubmitField('write log')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class InstanceActionForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    instance_action = HiddenField()
    submit = SubmitField('Sign In')
