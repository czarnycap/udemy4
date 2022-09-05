FROM python:3.8

# set a directory for the app
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

cmd ["python", "./flask_web_demo.py"]
