FROM python:3.7

MAINTAINER anudeepsamaiya@gmail.com

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project
COPY ./ /Project/app

# Set work directory
WORKDIR /Project/app

# Install dependencies
RUN pip install --upgrade pip && pip install pipenv \
    && pipenv install --system --deploy
