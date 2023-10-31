from flask import Flask, json
from handlers.authentication import LoginHandler
from flask import request

app = Flask(__name__)

login_handler = LoginHandler()
assert login_handler.validate_user("test","test")
@app.route('/', methods=['POST'])
def home():
    user_name = request.form['user_name']
    password = request.form['password']
    if login_handler.validate_user(user_name, password):
        print("OK")
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    return "Failed Login"

if __name__ == '__main__':
    app.run()
