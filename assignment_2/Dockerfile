FROM python:3.9-bullseye AS Base

COPY . /app
WORKDIR /app
RUN pip install flask

CMD [ "python", "app.py" ]