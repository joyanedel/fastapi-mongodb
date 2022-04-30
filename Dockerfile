FROM python:3.9

WORKDIR /src
COPY . /src/

RUN pip install -r requirements.txt --no-cache-dir && groupadd -g 1001 nonroot && useradd -r -u 1001 -g nonroot nonroot

EXPOSE 80