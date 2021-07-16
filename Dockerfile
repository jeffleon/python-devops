FROM python:3.8-slim-buster

# install enviroments dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        netcat \
    && apt-get -q clean

#set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

#install requirements
RUN pip3 install -r requirements.txt

#add app 
COPY . /usr/src/app

# run server
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]