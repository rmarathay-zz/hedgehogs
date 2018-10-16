# Hedgehogs

## How to run
* Clone the repository
* Navigate to hedgehogs/data_collection
The current pipeline currently looks something like this:
  xlsxDownloader --> xlsx2json.py --> json2mongodb.py
In order to run the program do the following:
* run `python xlsxDownload.py TICKER` to download the .xlsx files
* run `python xlsx2json.py FILE_NAME` to convert a .xlsx to .json
* run `python json2mongodb.py FILE_NAME USERNAME` to send the .json file to a running MongoDB server

## Run local version using Docker
* The first step is to set up the data_collection/db/config.py file
  * If you are on windows, and you are running docker through docker-machine:
    * run the command `docker-machine ip` and replace HOST with your result
  * If you are on mac or linux, use the command:
    * `ipconfig getifaddr en0` and replace HOST with your result
* To run the local postgres server and build and enter the python container's bash, use the command:
  * `docker-compose run data-collection`

## Development
* Become a developer on github
* Clone master, switch to develop
* `docker build -t hedgehogs .`
* `docker run -it hedgehogs /bin/bash`
* Execute all code in container

## Installation (deprecated)
* Install either Miniconda or Anaconda
  * Miniconda https://conda.io/miniconda.html
  * Anaconda https://www.anaconda.com/download/
* Configure the PATH system variable as such
  * `export PATH=~/miniconda2/bin:$PATH`
  * `export PATH=~/anaconda2/bin:$PATH`
* Verify Installation of Anaconda/Miniconda
  * `conda --version`
* Install Zipline
  * `conda install -c Quantopian zipline`
  * Yes, we are using Quantopian's API..
