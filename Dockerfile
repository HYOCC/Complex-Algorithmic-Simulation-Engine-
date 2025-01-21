FROM python:3.9-slim

WORKDIR /main

COPY requirements.txt . 

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Specify the command to run your application
CMD ["python", "main.py"]
