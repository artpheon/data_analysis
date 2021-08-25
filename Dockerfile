#image name
FROM ubuntu:latest

LABEL name="Artur N."
LABEL maintainer="idcdtokms@gmail.com"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install wget sudo bash vim software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    sudo apt-get -y install python3.8 python3-venv python3-pip python3-dev libpq-dev postgresql postgresql-contrib && \
    export PATH=$PATH:/usr/lib/postgresql/12/bin && \
    pip install --upgrade pip && \
    pip3 install openpyxl pandas psycopg2 sqlalchemy

# sudo service postgresql start
# then run 'sudo -u postgres -i' to get into databases
# or sudo -u postgres psql database-name
WORKDIR /var/www/hrobbin

COPY ./app/* /var/www/hrobbin/

RUN chmod 777 /var/www/hrobbin

EXPOSE 80 443

ENTRYPOINT /bin/bash