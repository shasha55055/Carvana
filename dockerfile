FROM python:3.9.7

ADD test.py .



CMD ["python", "./test.py"]