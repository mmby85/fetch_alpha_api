FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /fetch_alpha_api
WORKDIR /fetch_alpha_api

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./fetch_alpha_api /fetch_alpha_api

