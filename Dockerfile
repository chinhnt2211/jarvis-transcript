# Base image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements.txt to container
COPY ./requirements.txt /app/requirements.txt 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code to container
COPY . /app

ENV FLASK_APP=app

# Expose port
EXPOSE 5000

# Run the command to start the server
ENTRYPOINT [ "python" ]

CMD ["app.py"]

