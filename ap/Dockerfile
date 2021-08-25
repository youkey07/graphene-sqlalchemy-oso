FROM python:3.8.5

EXPOSE 5000

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --requirement /app/requirements.txt

RUN mkdir /var/log/app

COPY ./app /app

WORKDIR /app
CMD ["gunicorn", "app:app"]
