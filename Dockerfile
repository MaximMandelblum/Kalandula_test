FROM python:3.7-slim

RUN mkdir /kandula

COPY . /kandula/

WORKDIR /kandula
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/bin/bash", "bin/run"]
