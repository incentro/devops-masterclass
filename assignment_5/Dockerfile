FROM python:3.9-bullseye AS Base

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]
