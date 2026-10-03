FROM python:3.14.7

WORKDIR /app

COPY *.py .

CMD ["python","persistentauditor.py"]