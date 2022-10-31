FROM python:3.10.4

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install

ENTRYPOINT poetry run uvicorn src.main:app --host 0.0.0.0 --port ${API_PORT} --reload