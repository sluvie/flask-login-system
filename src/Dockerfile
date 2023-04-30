FROM python:3.8-slim

EXPOSE 5000

COPY ./ /app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r /app/requirement.txt --src /usr/local/src

WORKDIR /app

CMD [ "gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "server:app" ]