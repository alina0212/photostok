# Use the latest version of the official Python image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all local files to the working directory in the container
COPY . /app

# Install additional tools
RUN pip install coverage pytest pytest-cov

# Expose the port the web server will listen on
EXPOSE 8000

# Command to run your Django app using Gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]