import sqlite3

class Db:
    def __init__(self, path_to_db="data/users.db"):
        self.path_to_db=path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql:str, parameters: tuple=None, fetchone=False, fetchall= False, commit = False):
        "SELECT * FROM Users WHERE id=1"
        if not parameters:
            parameters=tuple()
        connection = self.connection

        connection.set_trace_callback(logger)
        cursor=connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()

        connection.close()

        return data

    def create_table_users(self):
        sql="""
        CREATE TABLE IF NOT EXISTS Users(
        id int NOT NULL,
        Name varchar(255) NOT NULL,
        admin int NOT NULL
        );
        """
        self.execute(sql, commit = True)

    def add_user(self, id:int, name:str, admin: int):
        sql = """
        INSERT or IGNORE INTO Users(id, name, admin) VALUES (?, ?, ?)
        """
        parameters = (id, name, admin)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql+=" AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
    def select_user(self, **kwargs):
        sql="SELECT * FROM Users WHERE "
        sql, parameters=self.format_args(sql, kwargs)
        print(self.execute(sql, parameters, fetchone=True))
        return self.execute(sql, parameters, fetchone=True)


    def count_users(self):
        return self.execute("SELECT COUNT (*) FROM Users;", fetchone=True)

    def delete_all_users(self):
        self.execute("DELETE FROM Users WHERE True", commit=True)

    def update_admin(self, id, admin):
        sql="UPDATE Users SET admin=? WHERE id=?"
        return self.execute(sql, parameters=(admin, id), commit=True)
#         0 - простой пользователь
#         1 - администратор бота
#         2 - администратор в режиме изменения данных


def logger(statement):
    print(f"""
_____________________________________
Executing:
{statement}
_____________________________________

""")