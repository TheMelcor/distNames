FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
add . /code/
RUN apt-get install -y python
RUN python get-pip.py
RUN pip install -r requirements.txt --no-index --find-links file:///code/
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]