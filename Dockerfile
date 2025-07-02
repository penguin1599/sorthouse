FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Container will listen on 5051
EXPOSE 5051

CMD ["python", "app.py"]
