FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src /opt/app/

WORKDIR /opt/app/

ENTRYPOINT ["python3"]
CMD ["/opt/app/main.py"]

