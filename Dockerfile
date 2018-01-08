FROM python:3.6-alpine
MAINTAINER Ahmad Harminto <harminto_ahmad@live.com>

ENV INSTALL_PATH /web_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:9090 --access-logfile - "web_app.app:create_app()"