# Hedgehogs
## How to run
* Clone the repository --> git clone https://github.com/rmarathay/hedgehogs.git  
* (if you don't have docker working pip install Django pip install Django-rest_framework)
* Run manage.py runserver 
* Navigate to url
* TODO hedgehogs.io

* At website, search for stock at top right corner search bar
* You can search by ticker or by stock name
* Upon search you will be prompted to log in if you have not loged in already 
* Currently display candelstick stock graph and regular graph aswell
* Tools page will be where algorithmic trading strategies will be created and tested 


## How to connect to database
* Install pgcli --> sudo apt-get install pgcli
* pgcli -h 206.189.181.163 -p 5432 -U rcos -d rcos -W
* password is hedgehogs_rcos when prompted
* \dt to see all tables
* TABLE [name of table you want to see dont put brackets]


## Run local version using Docker
* The first step is to set up the data_collection/db/config.py file
  * If you are on windows, and you are running docker through docker-machine:
    * run the command `docker-machine ip` and replace HOST with your result
  * If you are on mac or linux, use the command:
    * `ipconfig getifaddr en0` and replace HOST with your result
* To run the local postgres server and build and enter the python container's bash, use the command:
  * `docker-compose run data-collection`
* After the images are built the first time, the command should run a lot faster
* Note: The compose environment is set up to use volumes. You can change your local python code and the changes should be reflected from within the container

## Development (deprecated)
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


## How to run (deprecated)
* All code in the data_collection folder is depricated
* This was the code from previous RCOS years, it is no longer supported and does not work as intended
* If you would like to develop this on your own code at your own risk
* Clone the repository
* Navigate to hedgehogs/data_collection
The current pipeline currently looks something like this:
  xlsxDownloader --> xlsx2json.py --> json2mongodb.py
In order to run the program do the following:
* run `python xlsxDownload.py TICKER` to download the .xlsx files
* run `python xlsx2json.py FILE_NAME` to convert a .xlsx to .json
* run `python json2mongodb.py FILE_NAME USERNAME` to send the .json file to a running MongoDB server
