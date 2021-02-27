# pull official base image
FROM python:3.8.6

# mkdir bot
WORKDIR /bot

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /bot

CMD [ "python3", "app.py"]