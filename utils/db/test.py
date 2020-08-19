import asyncio

from utils.db.postgresql import Database


async def test():
    print("Создаем таблицу Пользователей...")
    await db.create_table_racers()
    print("Готово")

    print("Добавляем пользователей")

    await db.add_racer(1, "One", "email")
    await db.add_racer(2, "Vasya", "vv@gmail.com")
    await db.add_racer(3, "1", "1")
    await db.add_racer(4, "1", "1")
    await db.add_racer(5, "John", "john@mail.com")
    print("Готово")

    racers = await db.select_all_racers()
    print(f"Получил всех пользователей: {racers}")

    racer = await db.select_racer(Name="John", id=5)
    print(f"Получил пользователя: {racer}")


loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())
