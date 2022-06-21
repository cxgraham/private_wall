from flask_app import app
from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.controllers import users


class Message:
    db = 'private_wall_schema'

    def __init__(self, data):
        self.id = data['id']
        self.message_text = data['message_text']
        self.sender_id = data['sender_id']
        self.sender =data['sender']
        self.recipient_id = data['recipient_id']
        self.recipient = data['recipient']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CREATE 
    @classmethod
    def create_message(cls, data):
        if not cls.validate_message(data): 
            return False
        query = """
        INSERT INTO messages (message_text, sender_id, recipient_id)
        VALUES (%(message_text)s, %(sender_id)s, %(recipient_id)s)
        ;"""
        message_id = connectToMySQL(cls.db).query_db(query, data)
        return message_id

    # READ 
    @classmethod
    def get_user_messages(cls, data):
        query ="""
        SELECT users.first_name as recipient, users2.first_name as sender, messages.*
        FROM users LEFT JOIN messages ON users.id = messages.recipient_id
        LEFT JOIN users as users2 ON users2.id = messages.sender_id
        WHERE users.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages


    # UPDATE 


    # DELETE 
    @classmethod
    def delete_message_by_id(cls, id):
        data = {'id': id}
        query = """
        DELETE FROM messages
        WHERE messages.id = %(id)s
        """
        return connectToMySQL(cls.db).query_db(query, data)


    # VALIDATE
    @staticmethod
    def validate_message(data):
        is_valid = True
        if len(data['message_text']) < 5:
            flash('Message content must be at least five characters long', 'message')
            is_valid = False
        return is_valid