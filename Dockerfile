# Use latest Python runtime as a parent image
FROM continuumio/miniconda3

# Meta-data
LABEL maintainer="Shuyib" \
      description="Docker Data Science workflow: make the same environment as the speaker and create simulated insurance data."

# Set the working directory to /app
WORKDIR /app

# ensures that the python output is sent to the terminal without buffering
ENV PYTHONUNBUFFERED=TRUE

# Copy the current directory contents into the container at /app
COPY . /app

# create a virtual environment and activate it
RUN python3 -m venv pres-env

# activate virtual environment
CMD source pres-env/bin/activate

# install jupyter and extensions
RUN conda update --name base conda &&\
    conda install -c conda-forge diffprivlib

# Install the required libraries
RUN pip --no-cache-dir install --upgrade pip ipykernel &&\
pip --no-cache-dir install -r /app/requirements.txt

# Make port 9999 available to the world outside this container
EXPOSE 9999

# Create mountpoint
VOLUME /app

# Run jupyter when container launches
CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=9999", "--no-browser", "--allow-root"]
