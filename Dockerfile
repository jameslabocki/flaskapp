# Use Red Hat UBI 9 minimal as the base image
FROM registry.access.redhat.com/ubi9/ubi-minimal

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py

# Install Python and pip
RUN microdnf install -y python3 python3-pip && \
    microdnf clean all

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the app port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]

