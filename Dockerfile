FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
add . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]