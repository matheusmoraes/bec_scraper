FROM ubuntu:14.04

ENV BROWSER Firefox
ENV DISPLAY :99

WORKDIR /crawler

ADD . /crawler

#================================================
# Installations
#================================================

RUN apt-get update && apt-get install -y $BROWSER \
        build-essential libssl-dev python-setuptools \
        xvfb xz-utils zlib1g-dev python3-pip python3-dev \
        && cd /usr/local/bin \
        && ln -s /usr/bin/python3 python \
        && pip3 install --upgrade pip

RUN apt-get install -y ca-certificates curl firefox \
        && rm -fr /var/lib/apt/lists/* \
        && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz | tar xz -C /usr/local/bin \
        && apt-get purge -y ca-certificates curl


RUN pip3 install -r requirements.txt

#==================
# Xvfb + init scripts
#==================
# ADD libs/xvfb_init /etc/init.d/xvfb
# RUN chmod a+x /etc/init.d/xvfb
# 
# ADD libs/xvfb-daemon-run /usr/bin/xvfb-daemon-run
# RUN chmod a+x /usr/bin/xvfb-daemon-run

#============================
# Clean up
#============================
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# CMD xvfb-run --server-args="-screen 0 1024x768x24" python spider.py
