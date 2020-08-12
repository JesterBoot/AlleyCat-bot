from utils.db.sqlite import Database


def test():
    db = Database()
    db.create_table_racers()
    db.add_racer(1, "One", "email")
    db.add_racer(2, "Vasya", "vv@gmail.com")
    db.add_racer(3, 1, 1)
    db.add_racer(4, 1, 1)
    db.add_racer(5, "John", "john@mail.com")

    racers = db.select_all_racers()
    print(f"Получил всех пользователей: {racers}")

    racer = db.select_racer(Name="John", id=5)
    print(f"Получил пользователя: {racer}")

    racers = db.select_all_racers()
    print(f"Получил всех пользователей: {racers}")


test()
