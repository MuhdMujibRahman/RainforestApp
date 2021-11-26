FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /RainforestApp/App
COPY requirements.txt /RainforestApp/App
RUN pip install -r requirements.txt
COPY . /RainforestApp
