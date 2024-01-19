FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /app

CMD ["python", "launch.py"]