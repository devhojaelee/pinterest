FROM python:3.9.0
WORKDIR /home/
RUN git clone https://www.github.com/devhojaelee/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt
RUN echo "SECRET_KEY=django-insecure-0=$@*4&8a!^e=dye+yade^!&!evq1^x#r+x5t&%-w*)z@vi^kr" > .env

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8888

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]