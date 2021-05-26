FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3","-m","flask","run","--host=0.0.0.0"]