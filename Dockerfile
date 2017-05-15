FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
add . /code/
RUN apt-get install -y python
RUN apt-get install python-setuptools python-dev build-essential
RUN easy_install pip
RUN pip install /code/requirements.txt
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]