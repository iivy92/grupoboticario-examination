FROM python:3.10-slim-buster

RUN mkdir /opt/btc
WORKDIR /opt/btc
EXPOSE 8000

COPY requirements.txt requirements.txt
COPY . .


RUN apt-get update
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]