FROM python:3.9.0
WORKDIR /home/

RUN echo "testing4" #도커에서 캐시된 이미지를 갖고 있어서 앞단에 이런 의미없는걸 넣어줘야 처음부터 빌드를 한다.

RUN git clone https://www.github.com/devhojaelee/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt
RUN echo "SECRET_KEY=django-insecure-0=$@*4&8a!^e=dye+yade^!&!evq1^x#r+x5t&%-w*)z@vi^kr" > .env

RUN pip install gunicorn

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8888

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
