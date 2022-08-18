FROM python:latest

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

RUN apt update
RUN apt upgrade
RUN apt install libusb-1.0-0

ENTRYPOINT poetry run uvicorn src.main:app --host 0.0.0.0 --reload