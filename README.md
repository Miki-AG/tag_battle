# tag_battle

## Requirements
- Python 2.7
- You also need to install [pip](https://pypi.python.org/pypi/pip) and [virtualenv](https://virtualenv.pypa.io)

## Setup

### Get the code
git clone the repo with  the code in a local directory
```shell
https://github.com/Miki-AG/tag_battle.git
```

### Replicate python environment
1. Create a virtualenv
```shell
virtualenv ENV
```

2. Activate the new environment
```shell
source ./bin/activate
```

3. Move into the tag_battle folder and install all required packages
```shell
pip install -r requirements.txt
```

### Set up Twitter credentials

Enter your Twitter dev credentials in the file settings.py located in the ht_battle_project/ht_battle_project folder. You need to replace the below values with your own:
```shell
TWITTER_APP_KEY = 'xxxxxxxxx'
TWITTER_APP_KEY_SECRET = 'xxxxxxxxx'
TWITTER_ACCESS_TOKEN = 'xxxxxxxxx'
TWITTER_ACCESS_TOKEN_SECRET = 'xxxxxxxxx'
```

### Run manage.py
Move into tag_battle/ht_battle_project/ and run manage.py
```shell
python manage.py migrate
```

### Create an admin user
```shell
python manage.py createsuperuser
```

## Run the application

### Startup the dev server
```shell
python manage.py runserver
```
The console will show the status of all battles set up in the system every 10 seconds. Additional information wil be shown regarding status, data pulled out from Twitter and typos.

### Sign-in in the Admin Console
Use the admin user and password you have created to access the admin console in the below url:

http://127.0.0.1:8000/admin/

You can add, remove and edit battles throught the Admin Console.

### Public API
The application exposes an endpoint that provides information about battles in the url:

http://127.0.0.1:8000/api/battles/1/

(Replace the number at the end of the url with the id of the battle)

## Run the tests
```shell
python manage.py test
```

Built and tested in Mac OS Sierra 10.12.5

