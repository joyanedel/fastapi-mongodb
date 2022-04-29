FROM python:3.9

WORKDIR /src
COPY . /src/
RUN pip install -r requirements.txt
EXPOSE 80