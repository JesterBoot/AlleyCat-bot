import sqlite3


class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_racers(self):
        sql = """
        CREATE TABLE Racers (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            Second_Name varchar(255) NOT NULL,
            email varchar(255),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_racer(self, id: int, name: str, second_name: str, email: str = None):
        sql = """
        INSERT INTO Racers(id, Name, Second_Name, email) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, second_name, email), commit=True)

    def select_all_racers(self):
        sql = """
        SELECT * FROM Racers
        """
        return self.execute(sql, fetchall=True)

    def select_racer(self, **kwargs):
        sql = "SELECT * FROM Racers WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Racers;", fetchone=True)

    def update_user_email(self, email, id):
        sql = f"""
        UPDATE Racers SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_racers(self):
        self.execute("DELETE FROM Racers WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
