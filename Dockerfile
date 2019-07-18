FROM python:3.5

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY src/ .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--reload", "app:app"]
