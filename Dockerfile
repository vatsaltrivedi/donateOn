FROM ubuntu:12.10

# Install Python Setuptools
RUN apt-get install -y python-setuptools

# Install pip
RUN easy_install pip


# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
RUN pip install SQLAlchemy


# Bundle app source
ADD . /src

# Expose
EXPOSE  5000


