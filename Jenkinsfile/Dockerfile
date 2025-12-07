FROM jenkins/jenkins:lts

USER root

# تثبيت Docker CLI
RUN apt-get update && apt-get install -y \
    docker.io \
    python3 \
    python3-pip \
    git \
    curl \
    sudo \
    lsb-release && \
    apt-get clean

# تثبيت kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl

# إعطاء Jenkins الصلاحيات
RUN usermod -aG docker jenkins

USER jenkins