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
        && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz | tar xz -C /usr/local/bin

RUN pip3 install -r requirements.txt

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
RUN locale-gen en_US.UTF-8 \
  && dpkg-reconfigure --frontend noninteractive locales \
  && apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    language-pack-en

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

CMD xvfb-run --server-args="-screen 0 1024x768x24" python spider.py
