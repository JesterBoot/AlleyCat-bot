import asyncio

import asyncpg
from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncpg.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(user=config.PGUSER,
                                password=config.PGPASSWORD,
                                host=config.ip))

    '''Таблица для регистрации всех гонщиков'''

    async def create_table_racers(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Racers (
                id INT NOT NULL,
                Name VARCHAR (255) NOT NULL,
                Gender VARCHAR (255),
                Bicycle VARCHAR (255),
                Start_time VARCHAR (255),
                Finish_time VARCHAR (255),
                Total_time VARCHAR (255),
                PRIMARY KEY (id)
                );
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    async def add_racer(self, id: int, name: str):
        sql = """
        INSERT INTO Racers(id, Name) VALUES ($1, $2)
        """
        await self.pool.execute(sql, id, name)

    async def select_all_racers(self):
        sql = """
        SELECT * FROM Racers
        """
        return await self.pool.fetch(sql)

    async def select_racer(self, **kwargs):
        sql = """
        SELECT * FROM Racers WHERE 
        """
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_racers(self):
        return await self.pool.fetchval("SELECT COUNT (*) FROM Racers")

    async def update_racer_gender(self, gender: str, id: int):
        sql = '''
        UPDATE Racers SET Gender = $1 WHERE id =$2
        '''
        return await self.pool.execute(sql, gender, id)

    async def update_racer_bicycle(self, bicycle: str, id: int):
        sql = '''
        UPDATE Racers SET Bicycle = $1 WHERE id =$2
        '''
        return await self.pool.execute(sql, bicycle, id)

    async def start_time(self, start_time: str, id: int):
        sql = '''
        UPDATE Racers SET Start_time = $1 WHERE id =$2
        '''
        return await self.pool.execute(sql, start_time, id)

    async def finish_time(self, finish_time: str, id: int):
        sql = '''
        UPDATE Racers SET Finish_time = $1 WHERE id =$2
        '''
        return await self.pool.execute(sql, finish_time, id)

    async def total_time(self, total: str, id: int):
        sql = '''
        UPDATE Racers SET Total_time = $1 WHERE id =$2
        '''
        return await self.pool.execute(sql, total, id)

    async def delete_racers(self):
        await self.pool.execute('DELETE FROM Racers WHERE True')

    async def delete_table(self):
        await self.pool.execute('DROP TABLE Racers')


