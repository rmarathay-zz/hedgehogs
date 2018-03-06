FROM python:2.7.14-stretch
ADD . /data_collection
WORKDIR /data_collection
RUN pip install -r requirements.txt
CMD ["python", "/data_collection/xlsxDownloader.py"]
