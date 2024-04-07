# # Set a baseimage using python 3.11.8
# FROM  python:3.11.8

# # Create a directory within the container for the application
# WORKDIR /app

# # Copy the requirements.txt from the application to the container temp directory
# COPY requirements.txt temp/requirements.txt

# # Install pakages in the requirements.txt file recursively
# RUN python -m pip install --timeout 300000 -r requirements.txt

# # Copy all the files into the app directory
# COPY . /app

# # Expose port 8002 outside the container
# EXPOSE 8002

# # Run the fastAPI application
# CMD ['uvicorn','app:app', '--host','0.0.0.0','--port', 8002]

# Set a base image using Python 3.11.8

FROM python:3.11.8

# Create a directory within the container for the application
WORKDIR /app

# Create a temp directory in the container
RUN mkdir /temp

# Copy the requirements.txt from the application to the container temp directory
COPY requirements.txt temp/requirements.txt

# Install packages in the requirements.txt file recursively
RUN python -m pip install --timeout 300000 -r temp/requirements.txt

# Copy all the files into the app directory
COPY . /app

# Expose port 8002 outside the container
EXPOSE 8002

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]

