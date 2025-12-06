FROM ubuntu:22.04

RUN apt-get update && apt-get upgrade -y \ 
    && apt-get install -y --no-install-recommends \
        python3.10 \
        python3.10-venv \
        python3-pip \
        ca-certificates \
        bash \
        wget

COPY . /opt/website/
# COPY etc/website/ /etc/website/

RUN python3.10 -m venv /opt/website/venv 

ENV PATH="/opt/website/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /opt/website/requirements.txt \
    && pip install -e /opt/website/ 

WORKDIR /opt/website

# RUN python /opt/website/website/main.py