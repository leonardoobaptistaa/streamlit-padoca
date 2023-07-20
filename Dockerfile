FROM python:3.11.2-slim

RUN apt update && apt install -y --no-install-recommends locales

# Set the locale
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:en
ENV LC_ALL pt_BR.UTF-8

RUN apt install -y --no-install-recommends \
  build-essential \
  git

RUN pip install --upgrade pip

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app
