FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get clean

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "./main.py"]
