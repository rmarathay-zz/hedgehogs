# Hedgehogs
## How To Run
* Clone the repository ---> `git clone https://github.com/rmarathay/hedgehogs.git`
* Ensure latest update of pip or pip3 (if using Python3)
  * `pip install --upgrade pip`
* Navigate to hedgehogsRestApi to Install dependencies
  * `pip install -r requirements.txt`  
* Navigate to hedgehogsRestApi
  * Run `Python manage.py runserver` and follow instructions in terminal
* Navigate to URL
* TODO hedgehogs.io


## Website Usage
* At website, search for stock at top right corner search bar
* You can search by ticker or by stock name
* Upon search you will be prompted to log in if you have not logged in already
* Currently display candelstick stock graph and regular graph as well
* Tools page will be where algorithmic trading strategies will be created and tested


## How To Connect To Database
* Install pgcli --> `sudo apt-get install pgcli`
* `pgcli -h 206.189.181.163 -p 5432 -U rcos -d rcos -W`
* `\dt` to see all tables
* TABLE [name of table you want to see dont put brackets]


## Run Local Version Using Docker
* The first step is to set up the data_collection/db/config.py file
  * If you are on windows, and you are running docker through docker-machine:
    * run the command `docker-machine ip` and replace HOST with your result
  * If you are on mac or linux, use the command:
    * `ipconfig getifaddr en0` and replace HOST with your result
* To run the local postgres server and build and enter the python container's bash, use the command:
  * `docker-compose run data-collection`
* After the images are built the first time, the command should run a lot faster
* Note: The compose environment is set up to use volumes. You can change your local python code and the changes should be reflected from within the container
