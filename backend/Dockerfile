FROM python:alpine

# RUN apk add --no-cache --virtual .build-deps gcc musl-dev && pip install cython && apk del .build-deps gcc musl-dev
# RUN apk add --no-cache --update python3-dev  gcc build-base

# RUN adduser -D studentsapp

WORKDIR /home/studentsapp

COPY docker-requirements.txt docker-requirements.txt
# RUN python -m venv venv
# RUN venv/bin/pip install -r requirements.txt
# RUN venv/bin/pip install gunicorn
RUN pip install -r docker-requirements.txt


COPY app app
COPY migrations migrations
COPY students.py config.py docker-boot.sh ./
RUN chmod +x docker-boot.sh

ENV FLASK_APP students.py

# RUN chown -R studentsapp:studentsapp ./
# USER studentsapp

EXPOSE 5000
ENTRYPOINT ["./docker-boot.sh"]
