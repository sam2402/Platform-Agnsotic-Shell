FROM python:3.11-buster

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install git procps lsb-release libxml2-utils \
    && apt-get autoremove -y \
    && apt-get clean -y

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY . /comp0010

RUN chmod u+x /comp0010/sh
RUN chmod u+x /comp0010/tools/test
RUN chmod u+x /comp0010/tools/coverage
RUN chmod u+x /comp0010/tools/analysis

RUN chmod u+x /comp0010/tools/test_no_http
RUN chmod u+x /comp0010/tools/analysis_no_http
RUN chmod u+x /comp0010/tools/coverage_no_http

RUN cd /comp0010 && python -m pip install -r requirements.txt

ENV DEBIAN_FRONTEND=

EXPOSE 8000

