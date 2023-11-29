from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wftforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    # username attribute of the Stringfield class
    uname = StringField('Username', validators=[
                        DataRequired(), Length(min=2, max=20)])

    # email attribute of the Stringfield class
    email = StringField('Email', validators=[DataRequired(), Email()])

    # password attribute of Password class
    pwd = PasswordField('Password', validators=[DataRequired()])

    # password confirmation attribute of Password class
    pwd_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('pwd')])

    submit = SubmitField('Sign Up Here')


class LoginForm(FlaskForm):
    # login using email address
    email = StringField('Email', validators=[DataRequired(), Email()])

    pwd = PasswordField('Password', validators=[DataRequired()])

    # remember cookie to keep users logged in after browser is closed
    rem_me = BooleanField('Remember Me')

    submit = SubmitField('Login Here')
