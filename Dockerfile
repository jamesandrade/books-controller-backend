FROM python:3.10.6-slim-bullseye
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /code
EXPOSE 5000
CMD ["python", "app.py"]