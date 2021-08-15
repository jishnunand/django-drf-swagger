FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-drf-swagger
WORKDIR /django-drf-swagger
ADD requirements.txt /django-drf-swagger/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /django-drf-swagger/
EXPOSE 80 8000
