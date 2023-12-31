from flask import render_template, url_for, flash, redirect
from flaskmessenger.forms import RegistrationForm, LoginForm
from flaskmessenger import app, db
from flaskmessenger.models import User, Post

# Dummy date to iterate through using jinja for loops.
posts = [
    {
        'author': 'John Doe',
        'title': 'Message 1',
        'content': 'First post content',
        'date_posted': 'November 27th, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Message 2',
        'content': 'Second post content',
        'date_posted': 'November 27th, 2023'
    }
]


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # conditional to validate a successful registration
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # conditional to validate successful login
    if form.validate_on_submit():
        # fake data to create a successful login
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Please check username and password')
    return render_template("login.html", title='Login', form=form)
