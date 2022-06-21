from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message

# CREATE 
@app.route('/users/register', methods=['POST'])
def register():
    created_user = User.create_user(request.form)
    if created_user:
        return redirect('/users/profile')
    return redirect('/')

# READ 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/login', methods = ['POST'])
def login():
    if User.login(request.form):
        return redirect('/users/profile')
    return redirect('/')

@app.route('/users/profile')
def user():
    if 'user_id' not in session:
        return redirect('/')
    data = {'id': session['user_id']}
    user = User.get_user_by_id(data)
    users = User.get_all_users()
    messages = Message.get_user_messages(data)
    return render_template('user_profile.html', user = user, users = users, messages = messages )

# UPDATE 

# DELETE
@app.route('/users/logout')
def logout():
    session.clear()
    return redirect('/')