FROM python:latest

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run API server
ENTRYPOINT [ "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--reload" ]