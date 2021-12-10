import sqlite3
from functools import wraps

from flask import Flask, request, render_template, redirect, session, url_for, flash

app = Flask(__name__)

app.config.from_object('_config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test):
    @wraps(test)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return test(*args,**kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

#route handlers
@app.route('/logout/')
def logout():
    session.pop('logged_in',None)
    flash('Goodbye')
    return redirect(url_for('login'))

@app.route('/',methods=['GET','POSTS'])
def login():
    if request.method=='POST':
        if request.form['username'] != app.config['username'] or request.form['password'] != app.config['password']:
            error = 'Invlaid Credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('tasks'))
    return render_template('login.html')