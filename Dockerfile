FROM python:3.9

WORKDIR /src
COPY . /src/
CMD [ "pip", "install", "-r", "requirements.txt"]
EXPOSE 80