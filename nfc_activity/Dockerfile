FROM python:latest

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

RUN apt update -y
RUN apt upgrade -y
RUN apt install libusb-1.0-0 -y

ENTRYPOINT poetry run python main.py