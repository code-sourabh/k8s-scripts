FROM --platform=linux/amd64 python:3.8-slim

WORKDIR /

COPY ./scale/requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./scale/* .

ENTRYPOINT [ "/bin/bash" ]