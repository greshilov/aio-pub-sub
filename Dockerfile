FROM       python:3.6
MAINTAINER Slavik Greshilov

COPY . /aps
RUN pip install -r /aps/etc/requirements.txt

WORKDIR /aps
ENV PB_DEBUG=false

CMD ["python", "server.py"]