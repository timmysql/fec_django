# fec_django

## Overview
Work in progress utility for downloading and researching campaign finance data from the Federal Election Commission's API.

Currently working on building a simple and efficient data loading system using python data classes, sqlmodel and postgresql.

## Setup

### Download or Clone github repo

### Create Virtual Environment


### Install Requirements
- pip install -r requirements.txt


## Setup .env file
- see .env_example in root folder
- create .env file in root folder
- in .env, enter...

```
fec_api_key = "YOUR_API_KEY_GOES_HERE"
host = "YOUR_DB_IP_ADDRESS_GOES_HERE"
database = "YOUR_DATABASE_NAME_GOES_HERE"
user = "YOUR_DB_USERNAME_GOES_HERE"
password = "YOUR_DB_PASSWORD_GOES_HERE"
```

## Setup database requirements
- run setup_requirements.py
- the python script referenced creates... 
  1. database
  2. tables
  3. inserts states into states table