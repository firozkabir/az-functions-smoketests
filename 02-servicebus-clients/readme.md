# Smoke Test Service Bus from On-Premises Server(s)

## How to deploy and run 
* Checkout from git: `git clone git@github.com:firozkabir/yu-ssrp-azure-eip-smoketests-2022.git`
* Go to the 02-service `02-servicebus-clients` directory
* Rename config.ini.sample file to create the config.ini file `mv config.ini.sample config.ini`
* Update `CONNECTION_STR` and `QUEUE_NAME` parameters in `config.ini`
* Create virtual environment `virtualenv -p /usr/bin/python3 .venv`
* Install requirements `pip3 install -r requirements.txt`
* Activate virtual environment `source ./venv/bin/actiavate`
* Run producer `python3 scs_producer.py`
* Run consumer `python3 scs_consumer.py`

