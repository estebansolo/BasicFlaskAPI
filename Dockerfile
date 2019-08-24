FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV PYTHONPATH /app/
ENV MYSQL_HOST 192.168.55.2
ENV MYSQL_DATABASE merqueo
ENV MYSQL_USER dbuser
ENV MYSQL_PASSWORD m3rqu30!

EXPOSE 5000

CMD flask run --host=0.0.0.0
