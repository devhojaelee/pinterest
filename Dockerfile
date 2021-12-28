FROM python:3.9.0
WORKDIR /home/
RUN git clone https://www.github.com/devhojaelee/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt
RUN echo "SECRET_KEY=django-insecure-0=$@*4&8a!^e=dye+yade^!&!evq1^x#r+x5t&%-w*)z@vi^kr" > .env


RUN python manage.py migrate

EXPOSE 8888

CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]