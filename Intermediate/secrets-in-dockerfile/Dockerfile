FROM python:3.9

# Embedding secret in ENV
ENV API_KEY=supersecretapikey123

# Also writing it into a file in a separate layer
RUN echo "API_KEY=supersecretapikey123" > /root/.env

# Copy your app
COPY app.py /app/app.py

WORKDIR /app
CMD ["python", "app.py"]
