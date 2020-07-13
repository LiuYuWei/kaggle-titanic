FROM ubuntu:18.04

#Setting timezone
ENV TZ Asia/Taipei

#Add Python lib version 
ADD ./requirements.txt /root/tmp/requirements.txt

#Construct the home directory and work directory
RUN addgroup --gid 1001 app 
RUN useradd -u 1001 \
            -G app \
            -d /home/app/workdir \
            -s /sbin/nologin \
            -g app \
            app

RUN apt-get update && \  
    apt-get install -y python3.6 \
    python3.6-dev \
    python3-pip \
    libyaml-cpp-dev \
    libyaml-dev \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN pip3 --no-cache-dir install -r /root/tmp/requirements.txt

#Create an app user for the application usage
ENV HOME=/home/app/
ENV APP_HOME=/home/app/workdir/

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
RUN chown -R app:app $APP_HOME

#Project data and code
COPY . $APP_HOME

EXPOSE 8000
ENV PROJECT_PATH=$APP_HOME
ENV SERVICE_PORT=8000
ENV SERVICE_IP=0.0.0.0:${SERVICE_PORT}

#Change User
USER app

#Run api code
ENTRYPOINT [ "python", "main.py", "--mode", "serving" ] 