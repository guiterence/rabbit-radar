FROM python:3.11.0-slim

WORKDIR /usr/src/app

RUN pip install --upgrade pip==22.3.1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "notify.py"]
