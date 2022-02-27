FROM python:3.9.7

ADD test.py .

COPY sample.txt .

CMD ["python", "./test.py"]
