# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files to the container
COPY requirements/prod.txt requirements/prod.txt

# Install any needed packages specified in requirements files
RUN pip install --no-cache-dir -r requirements/prod.txt

# Install system dependencies for Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxi6 \
    libxrender1 \
    libxrandr2 \
    libxfixes3 \
    libxcursor1 \
    libxinerama1 \
    libxcomposite1 \
    libasound2 \
    libxdamage1 \
    libxtst6 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# Copy the entire FastAPI project to the container
COPY /src /app

# Expose the port that your FastAPI app will run on
EXPOSE 8080

# Define environment variables if needed
# ENV MY_ENV_VARIABLE=my_value

# Run main.py when the container launches
CMD ["uvicorn", "--host=0.0.0.0", "--port=8080", "main:app"]
