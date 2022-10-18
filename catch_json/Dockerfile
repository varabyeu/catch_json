FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000