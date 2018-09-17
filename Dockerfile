FROM python:3.6-slim-jessie

ENV REPO /repo
ENV VARIANT $REPO/variant
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes

SHELL ["/bin/bash", "-c"]
WORKDIR $VARIANT
COPY . $VARIANT
RUN cd $VARIANT

RUN apt-get update \
	&& apt-get install -y less vim \
	&& pip install -U pip \
	&& pip install -U setuptools \
	&& apt-get install -y apt-utils \
	&& pip install -r requirements.txt \
	&& pip install -U pyspark
ENV EDITOR vim


CMD ["/bin/bash", "-l"]
