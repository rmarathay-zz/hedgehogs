#!/bin/bash
echo "Start!"

sh ./run_download.sh
sh ./run_xlsx2json.sh
sh ./run_json2mongodb.sh



