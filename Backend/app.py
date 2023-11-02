from flask import Flask, json
from handlers.authentication import LoginHandler
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    return json.dumps({'success': True, 'status': 200, 'response': True})
    # todo: Resolve this error. Able to open database from Tests but not app
    # user_name = request.form['user_name']
    # password = request.form['password']
    # login_handler = LoginHandler()
    # if login_handler.validate_user(user_name, password):
    #     return json.dumps({'success': True, 'status':200, 'response':True})
    # return "Failed Login"


if __name__ == '__main__':
    app.run()
