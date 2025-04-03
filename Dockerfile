FROM python:3.14.0a6-alpine3.21

WORKDIR /src

COPY src/*requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD ["python3", "app.py"]