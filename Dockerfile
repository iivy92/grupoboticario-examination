FROM python:3.10-slim-buster

RUN mkdir /opt/btc
WORKDIR /opt/btc

COPY requirements.txt requirements.txt
COPY . .


RUN apt-get update
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--reload"]