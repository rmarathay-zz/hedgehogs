FROM python:3.6-slim-jessie

ENV REPO /repo
ENV HEDGEHOGS $REPO/hedgehogs
ENV SLUGIFY_USES_TEXT_UNIDECODE=yes

SHELL ["/bin/bash", "-c"]
WORKDIR $HEDGEHOGS
COPY . $HEDGEHOGS
RUN cd $HEDGEHOGS

VOLUME .:/repo/hedgehogs

RUN apt-get update \
	&& apt-get install -y less vim \
	&& pip install -U pip \
	&& pip install -U setuptools \
	&& apt-get install -y apt-utils \
	&& pip install -r requirements.txt



CMD ["python", "manage.py", "runserver"]
