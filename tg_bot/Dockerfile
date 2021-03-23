# pull official base image
FROM python:3.9.0

# mkdir bot
WORKDIR /bot

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD [ "python3", "app.py"]