FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y git python3 python3-pip && rm -rf varlibaptlists

EXPOSE 8080

USER jenkins
