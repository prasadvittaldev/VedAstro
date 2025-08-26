FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY vedastro_core /app/vedastro_core
COPY vedastro_api /app/vedastro_api
EXPOSE 8000
CMD ["uvicorn", "vedastro_api:app", "--host", "0.0.0.0", "--port", "8000"]
