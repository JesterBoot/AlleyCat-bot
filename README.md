# AlleyCat-bot
Телеграм бот, с помощью которого вы сможете провести [аллейкат-гонку](https://en.wikipedia.org/wiki/Alleycat_race).

## Установка и использование
### Скачайте и установите зависимости
Выполните в консоли:
```
git clone https://github.com/StGrail/AlleyCat-bot.git
cd AlleyCat-bot
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
### Выполните настройку
Переименуйте файл .env.example в .env и замените  следующие данные:
```
BOT_TOKEN = токен вашего тг-бота
DJANGO_SECRET_KEY = django secret key

DATABASE_NAME = имя базы данных
PGUSER = имя юзера для базы данных
PGPASSWORD = пароль для базы данных
DATABASE_HOST = db если используете docker-compose
DATABASE_HOST = localhost если запускаете без docker-compose

ADMINS = id админов в телеграм
```
### Запустите бота
```
python3 app.py
```
### Или с docker-compose:
#### Запускается база данных, тг-бот и веб-приложение по адресу: [0.0.0.0:8000](0.0.0.0:8000)
```
sudo docker-compose build
sudo docker-compose up
```

## Участие в проекте
Пулл реквесты приветствуются. Для значительных изменений, пожалуйста,  сначала задайте вопрос на гитхаб для обсуждения того, что бы Вы хотели изменить.
## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)