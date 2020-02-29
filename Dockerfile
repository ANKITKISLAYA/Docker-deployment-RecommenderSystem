# Use the Python3.7.2 image
# FROM python:3.7.2-stretch

FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /flask

# Copy the current directory contents into the container at /app 
ADD . /flask

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["python", "app.py"]