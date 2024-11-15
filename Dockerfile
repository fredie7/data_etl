# parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "load_to_postgres.py"]
