from flask import Flask

app = Flask(__name__)


def home():
    user_name = request.form['user_name']
    password = request.form['password']
    if login_handler.validate_user(user_name, password):


if __name__ == '__main__':
    app.run()
