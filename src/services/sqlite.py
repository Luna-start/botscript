
import sqlite3

db_file = 'dbscript.db'

class DataBase:

    def __init__(self, connect):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def add_user(self, user_id, user_name, datee):
        with self.connect:
            return self.cursor.execute("""INSERT INTO users (user_id, user_name, datee) VALUES (?, ?, ?)""",
                                       [user_id, user_name, datee])

    async def update_age(self, age, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET age=(?) WHERE user_id=(?)""",
                                       [age, user_id])

    async def get_age(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT age FROM users WHERE user_id=(?)""",
                                       [user_id]).fetchone()

    async def get_date_of_birth(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT date_of_birth FROM users WHERE user_id=(?)""",
                                       [user_id]).fetchone()

    async def update_greetings_status(self, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET greetings_are_needed=(?) WHERE user_id=(?)""",
                                       [0, user_id])

    async def get_greetings_status(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT greetings_are_needed FROM users WHERE user_id=(?)""",
                                       [user_id]).fetchone()

    async def update_name(self, name, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET name=(?) WHERE user_id=(?)""",
                                       [name, user_id])

    async def update_message_count(self, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET message_count=(+=1) WHERE user_id=(?)""",
                                       [user_id])

    async def get_statistics(self, date_st):
        with self.connect:
            return self.cursor.execute("""SELECT user_id FROM users WHERE datee=(?)""",
                                       [date_st]).fetchall()

    async def get_users(self):
        with self.connect:
            return self.cursor.execute("""SELECT age, user_id FROM users""").fetchall()

    async def update_switch(self, status, user_id):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET switch=(?) WHERE user_id=(?)""",
                                       [status, user_id])

    async def get_switch_status(self, user_id):
        with self.connect:
            return self.cursor.execute("""SELECT switch FROM users WHERE user_id=(?)""",
                                       [user_id]).fetchone()