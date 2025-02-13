FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python-setuptools \
    python3-dev \
    build-essential \
    python3-pip \
    stgit \
    jq \
    python3-simplejson \
    python3-testresources \
    libpq-dev \
    curl

RUN pip3 install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

#Install Java
RUN /bin/bash -c "export TZ=Indian"
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y openjdk-11-jre-headless
RUN apt-get install -y default-jre
RUN /bin/bash -c "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin/java"


#Install Google Cloud related packages
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg add - && \
    apt-get update && apt-get install google-cloud-sdk  google-cloud-sdk-gke-gcloud-auth-plugin

# Gcloud Auth plugin config
RUN echo  "export USE_GKE_GCLOUD_AUTH_PLUGIN=True" >> .bashrc
RUN /bin/bash -c "source .bashrc"
RUN /bin/bash -c "export USE_GKE_GCLOUD_AUTH_PLUGIN=True"

# Download and install kubectl
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.26.0/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/

# Add ssh keys
#COPY ssh/id_rsa /root/.ssh/id_rsa
#COPY ssh/id_rsa.pub /root/.ssh/id_rsa.pub
Run echo "image got built"

CMD ["/bin/bash"]
