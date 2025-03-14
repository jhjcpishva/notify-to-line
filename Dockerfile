FROM python:3.11-slim
LABEL org.opencontainers.image.source="https://github.com/jhjcpishva/notify-to-line"

RUN mkdir /app/
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY *.py /app/.
CMD ["python", "main.py"]

