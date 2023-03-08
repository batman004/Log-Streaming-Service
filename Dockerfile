FROM python:3.9.15-slim

WORKDIR /log-server

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /app /log-server/app

RUN mkdir --p /log-server/logs

EXPOSE 8000

CMD [ "python", "app/main.py" ]
