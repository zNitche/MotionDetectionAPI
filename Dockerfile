FROM python:3.9

COPY . /PiMotionDetectionAPI
WORKDIR /PiMotionDetectionAPI

RUN apt update && apt -y install nano

RUN pip3 install -r requirements.txt -v

CMD python3 app.py