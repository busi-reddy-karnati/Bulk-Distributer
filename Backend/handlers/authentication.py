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
            cur.close()
            return False
        cur.close()
        return True
