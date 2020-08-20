import asyncio

import asyncpg
from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncpg.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(user=config.PGUSER,
                                password=config.PGPASSWORD,
                                host=config.ip))

    async def create_table_racers(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Racers (
                id INT NOT NULL,
                Name VARCHAR (255) NOT NULL,
                Gender VARCHAR (255),
                Bicycle VARCHAR (255),
                PRIMARY KEY (id)
                );
"""
        await self.pool.execute(sql)
        # sql = '''
        # CREATE TABLE IF NOT EXISTS Racers (
        # id INT NOT NULL,
        # Name VARCHAR (255) NOT NULL,
        # Last_name VARCHAR (255) NOT NULL,
        # Gender VARCHAR (255),
        # Fixie BOOLEAN,
        # First_location BOOLEAN,
        # First_photo VARCHAR (255),
        # Second_location BOOLEAN,
        # Second_photo VARCHAR (255),
        # Third_location BOOLEAN,
        # Third_photo VARCHAR (255),
        # Fourth_location BOOLEAN,
        # Fourth_photo VARCHAR (255),
        # Fifth_location BOOLEAN,
        # Fifth_photo VARCHAR (255),
        # Sixth_location BOOLEAN,
        # Sixth_photo VARCHAR (255),
        # Seventh_location BOOLEAN,
        # Seventh_photo VARCHAR (255),
        # Eighth_location BOOLEAN,
        # Eighth_photo VARCHAR (255),
        # Time VARCHAR (255),
        # PRIMARY KEY(id))
        # '''

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    # async def add_racer(self, id: int, name: str, last_name: str, gender: str = None, fixie: bool = None,
    #                     first_location: bool = None, first_photo: str = None, second_location: bool = None,
    #                     second_photo: str = None, third_location: bool = None, third_photo: str = None,
    #                     fourth_location: bool = None, fourth_photo: str = None, fifth_location: bool = None,
    #                     fifth_photo: str = None, sixth_location: bool = None, sixth_photo: str = None,
    #                     seventh_location: bool = None, seventh_photo: str = None, eight_location: bool = None,
    #                     eight_photo: str = None, time: str = None):
    # sql = '''INSERT INTO (id, name, last_name, gender, fixie, first_location, first_photo, second_location,
    # second_photo, third_location, third_photo, fourth_location, fourth_photo, fifth_location, fifth_photo,
    # sixth_location, sixth_photo, seventh_location, seventh_photo, eight_location, eight_photo, time) VALUES ($1,
    # $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22)'''
    async def add_racer(self, id: int, name: str):

        sql = """
        INSERT INTO Racers(id, Name) VALUES ($1, $2)
        """
        await self.pool.execute(sql, id, name)

        # await self.pool.execute(sql, id, name, last_name, gender, fixie, first_location, first_photo,
        #                         second_location, second_photo, third_location, third_photo, fourth_location,
        #                         fourth_photo, fifth_location, fifth_photo, sixth_location, sixth_photo,
        #                         seventh_location, seventh_photo, eight_location, eight_photo, time)

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

    async def delete_racers(self):
        await self.pool.execute('DELETE FROM Racers WHERE True')

    async def delete_table(self):
        await self.pool.execute('DROP TABLE Racers')
