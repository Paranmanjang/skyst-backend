# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files to the container
COPY requirements/prod.txt requirements/prod.txt

# Install any needed packages specified in requirements files
RUN pip install --no-cache-dir -r requirements/prod.txt

# Install required packages and utilities for Chrome and Chromedriver
RUN apt-get update -qq -y && \
    apt-get install -y \
        libasound2 \
        libatk-bridge2.0-0 \
        libgtk-4-1 \
        libnss3 \
        xdg-utils \
        wget \
        unzip && \
    wget -q -O /opt/chrome-linux64.zip https://bit.ly/chrome-linux64-121-0-6167-85 && \
    unzip /opt/chrome-linux64.zip -d /opt/ && \
    rm /opt/chrome-linux64.zip && \
    ln -s /opt/chrome/chrome /usr/local/bin/chrome && \
    wget -q -O /opt/chromedriver-linux64.zip https://bit.ly/chromedriver-linux64-121-0-6167-85 && \
    unzip /opt/chromedriver-linux64.zip -d /opt/ && \
    rm /opt/chromedriver-linux64.zip && \
    mv /opt/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chrome /usr/local/bin/chromedriver


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the entire FastAPI project to the container
COPY /src /app

# Expose the port that your FastAPI app will run on
EXPOSE 8080

# Define environment variables if needed
# ENV MY_ENV_VARIABLE=my_value

# Run main.py when the container launches
CMD ["uvicorn", "--host=0.0.0.0", "--port=8080", "main:app"]
