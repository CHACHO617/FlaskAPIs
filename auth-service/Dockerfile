# Use a minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Install dependencies
RUN pip install Flask PyJWT
RUN pip install jaeger-client flask-opentracing

# Expose the app port
EXPOSE 5000

# Run the app
CMD ["python", "auth_service.py"]
