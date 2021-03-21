FROM alpine:3.8
ENV PYTHONUNBUFFERED 1
RUN apk update && apk upgrade && apk --update add \
    linux-headers musl-dev gcc zlib-dev jpeg-dev \
    python3 python3-dev postgresql-dev \
    nodejs nodejs-npm  libsass sassc
RUN pip3 install uwsgi pipenv
RUN npm install -g yuglify
RUN mkdir /website
WORKDIR /website
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system
COPY package.json .
COPY package-lock.json .
RUN npm install
Add . /website/
ENV DJANGO_ENV=production
EXPOSE 8000
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT /docker-entrypoint.sh
