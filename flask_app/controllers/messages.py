from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.message import Message
from flask_app.models.user import User

# CREATE
@app.route('/messages/send', methods=['POST'])
def send_message():
    if 'user_id' in session:
        Message.create_message(request.form)
        return redirect('/users/profile')
    return redirect('/')

# READ 


# UPDATE 


# DELETE
@app.route('/messages/delete/<int:id>', methods= ['POST'])
def delete_message(id):
    if 'user_id' in session:
        Message.delete_message_by_id(id)
        return redirect('/users/profile')
    return redirect('/')