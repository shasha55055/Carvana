FROM python:3.9.7

ADD Main.py .

COPY sample.txt .

CMD ["python", "./test.py"]
