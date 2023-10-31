import sqlite3 as sql

class LoginHandler:
    def __init__(self):
        pass

    def validate_user(self, user_name, password):
        con = sql.connect("../database/database.db")
        cur = con.cursor()
        assert isinstance(user_name, str)
        assert isinstance(password, str)
        cur.execute(f"select * from login_details where user_id={user_name} and password={password}")
        user = cur.fetchone()
        if not user:
            return False
        return True