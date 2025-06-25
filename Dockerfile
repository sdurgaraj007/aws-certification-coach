# Python Docker image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy rest of the application code into the container
COPY main.py /app/main.py

# Expose the Streamlit port
EXPOSE 8501

# Set the entrypoint and run the application
ENTRYPOINT [ "streamlit", "run", "main.py" ]