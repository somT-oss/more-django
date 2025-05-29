<<<<<<< HEAD
FROM python:3.11-alpine 
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements/local_requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======
FROM python:3.11.9

WORKDIR /communely

COPY requirements/prod_requirement.txt /communely/requirements.txt

RUN pip install -r /communely/requirements.txt

RUN apt-get update \ 
    && apt-get -y install libpq-dev gcc 

RUN apt-get install -y postgresql postgresql-contrib

COPY . /communely/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8080", "config.wsgi:application"]
>>>>>>> 933c2c75f1245c04e41e5864263b2adab79cf79f
