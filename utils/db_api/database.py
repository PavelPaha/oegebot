import sqlite3

class Database:
    def __init__(self, path_to_db="data/main.db", name="default", count=0):
        self.path_to_db=path_to_db
        self.name=name
        self.count=count

    def initialize(self):
        self.create_table()
        print(self.count_numbers())
        for i in range(self.count_numbers()[0], self.count+1):
            self.add_number(i, "Нет данных(")

    def execute(self, sql:str, parameters: tuple=None, fetchone=False, fetchall= False, commit = False):
        "SELECT * FROM Math_numbers WHERE id=1"
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

    def create_table(self):
        sql=f"""
        CREATE TABLE IF NOT EXISTS {self.name}_numbers(
        num int NOT NULL,
        information TEXT NOT NULL,
        UNIQUE(num, information));
        """
        self.execute(sql, commit = True)

    def add_number(self, num:int, information:str):
        sql = f"""
        INSERT or IGNORE INTO {self.name}_numbers(num, information) VALUES (?, ?)
        """
        parameters = (num, information)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_numbers(self):
        sql = f"SELECT * FROM {self.name}_numbers"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql+=" AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_number(self, **kwargs):
        sql=f"SELECT * FROM {self.name}_numbers WHERE "
        sql, parameters=self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)


    # def select_number(self, number):
    #     {"num": number}
    #

    def count_numbers(self):
        return self.execute(f"SELECT COUNT (*) FROM {self.name}_numbers;", fetchone=True)

    def update_text(self, num, information):
        sql=f"UPDATE {self.name}_numbers SET information=? WHERE num=?"
        return self.execute(sql, parameters=(information, num), commit=True)

    def delete_all(self):
        self.execute(f"DELETE FROM {self.name}_numbers WHERE True", commit=True)

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)







class Reference_information:
    def __init__(self, path_to_db="data/refinf_none.db", name="default", count=0):
        self.path_to_db=path_to_db
        self.name=name
        self.count=count

    def initialize(self):
        self.create_table()
        print(self.count_numbers())
        default_s = "Вы можете предложить добавить сюда новую информацию, написав команду /new_content"
        for i in range(1, self.count):
            self.add_number(i, default_s)

    def execute(self, sql:str, parameters: tuple=None, fetchone=False, fetchall= False, commit = False):
        "SELECT * FROM Math_numbers WHERE id=1"
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

    def create_table(self):
        sql=f"""
        CREATE TABLE IF NOT EXISTS {self.name}_numbers(
        lesson INT NOT NULL,
        information TEXT NOT NULL,
        UNIQUE(num, information));
        """
        self.execute(sql, commit = True)

    def add_number(self, lesson:int, information:str):
        sql = f"""
        INSERT or IGNORE INTO {self.name}_numbers(lesson, information) VALUES (?, ?)
        """
        parameters = (lesson, information)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all(self):
        sql = f"SELECT * FROM {self.name}_numbers"
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql+=" AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_number(self, **kwargs):
        sql=f"SELECT * FROM {self.name}_numbers WHERE "
        sql, parameters=self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)


    # def select_number(self, number):
    #     {"num": number}
    #

    def count_numbers(self):
        return self.execute(f"SELECT COUNT (*) FROM {self.name}_numbers;", fetchone=True)

    def update_text(self, lesson, information):
        sql=f"UPDATE {self.name}_numbers SET information=? WHERE lesson=?"
        return self.execute(sql, parameters=(information, lesson), commit=True)

    def delete_all(self):
        self.execute(f"DELETE FROM {self.name}_numbers WHERE True", commit=True)

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)



def logger(statement):
    print(f"""_____________________________________
Executing:
{statement}""")


