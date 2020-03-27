RUN adduser -D studentsapp

WORKDIR /home/studentsapp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY students.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP students.py

RUN chown -R studentsapp:studentsapp ./
USER studentsapp

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
