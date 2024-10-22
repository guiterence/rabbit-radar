FROM python:3.11.0-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    python3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY . .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
