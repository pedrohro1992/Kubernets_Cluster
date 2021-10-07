FROM jenkins/jenkins



# install Maven
USER root

RUN apt-get update && apt-get install -y python3 python3-pip jq
RUN pip3 install awscli
RUN rm -rf /var/lib/apt/lists/*

