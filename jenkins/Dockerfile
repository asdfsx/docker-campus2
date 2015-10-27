FROM ubuntu:14.04

RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update && \
    apt-get install -y curl daemon psmisc wget openjdk-7-jre-headless git-core unzip apache2-utils && \
    wget http://pkg.jenkins-ci.org/debian/binary/jenkins_1.609_all.deb 

RUN dpkg -i jenkins_1.609_all.deb

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
    DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]') && \
    CODENAME=$(lsb_release -cs) && \
    echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" | tee /etc/apt/sources.list.d/mesosphere.list && \
    apt-get -y update && \
    apt-get install -y mesos && \
    locale-gen en_US.UTF-8

RUN mkdir /mnt/mesos && \
    mkdir /mnt/mesos/sandbox

ENV JENKINS_HOME /var/lib/jenkins

COPY plugins.sh /var/lib/jenkins/plugins.sh
COPY plugins.txt /var/lib/jenkins/plugins.txt
RUN /bin/bash /var/lib/jenkins/plugins.sh  /var/lib/jenkins/plugins.txt 

VOLUME /var/lib/jenkins

