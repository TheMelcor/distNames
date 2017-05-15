FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
add . /code/
RUN "pip install requirements.txt"
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]