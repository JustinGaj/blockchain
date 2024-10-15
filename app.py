#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

from sqlhelpers import *
from forms import *

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crypto'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def log_in_user(username): 
    pass

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = Registerform(request.form)
    users = Table("users", "name", "email", "username", "password")

    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        name = form.name.data

        if True: # check if new user
            password = sha256_crypt.encrypt(form.password.data)
            users.insert(name,email,username,password)
            log_in_user(username)
            return redirect(url_for('dashboard'))
        else:
            flash('User already exists', 'danger')
            return redirect('register')
        
    return render_template('register.html', form=form)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug = True)