FROM python:3.11.9

WORKDIR /communely/

COPY requirements/prod_requirement.txt /communely/requirements.txt

RUN pip install -r /communely/requirements.txt

RUN apt-get update \ 
    && apt-get -y install libpq-dev gcc 

RUN apt-get install -y postgresql postgresql-contrib

COPY . /communely/

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8080", "config.wsgi:application"]