# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files to the container
COPY requirements/prod.txt requirements/prod.txt

# Install any needed packages specified in requirements files
RUN pip install --no-cache-dir -r requirements/prod.txt

# Install required packages and utilities for Chrome and Chromedriver
# Install required packages for Google Chrome and wget to download Chrome and Chromedriver
RUN apt-get update -qqy && apt-get -qqy install \
    wget \
    unzip \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf-2.0-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    libvulkan1 \
    libgbm1 \
    libgtk-3-0

# Download and install Google Chrome.
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Set ChromeDriver version
ENV CHROMEDRIVER_VERSION 97.0.4692.71

# Download and install ChromeDriver
RUN wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip /chromedriver/chromedriver* -d /usr/local/bin/ \
    && rm /chromedriver/chromedriver_linux64.zip

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
