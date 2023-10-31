import sqlite3 as sql

class LoginHandler:
    def __init__(self):
        pass

    def validate_user(self, user_name, password):
        # todo: Resolve problem with connection. Update.
        con = sql.connect("../database/database.db")
        cur = con.cursor()
        assert isinstance(user_name, str)
        assert isinstance(password, str)
        cur.execute("select * from login_details where user_id=? and password=?",(user_name, password))
        user = cur.fetchone()
        if not user:
            return False
        return True

# todo: Change to central test location
test_login_handler = LoginHandler()
assert test_login_handler.validate_user("test", "test")