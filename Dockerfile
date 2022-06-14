FROM python:3.10-alpine3.16
WORKDIR /code
COPY  pywww/ /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt
