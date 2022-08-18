FROM python:latest

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT poetry run python main.py