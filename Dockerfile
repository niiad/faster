FROM python:3.12

WORKDIR /usr/src/app

ADD . /usr/src/app

CMD ["python", "api.py"]