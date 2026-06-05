# Use slim Python image — smaller = faster pulls, fewer vulnerabilities
FROM python:3.12-slim

WORKDIR /app

# Copy deps first — Docker layer caching speeds up rebuilds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run with gunicorn in production (not flask dev server)
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]