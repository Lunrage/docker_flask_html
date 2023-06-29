FROM python:3.9.15-alpine
WORKDIR /my_app2
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev
RUN pip install --upgrade pip
COPY requirements.txt /my_app2/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /my_app2
CMD ["python", "./hello.py", "--v1", "4", "--v2", "6", "--op", "*"]