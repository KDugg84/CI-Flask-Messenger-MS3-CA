from flask import render_template
from forms import RegistrationForm, LoginForm
from flaskmessenger import app, db

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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)
