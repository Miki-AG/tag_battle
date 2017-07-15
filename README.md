# tag_battle

Tested in Mac OS Sierra 10.12.5



## Requirements
- Python 2.7
- You also need to install [pip](https://pypi.python.org/pypi/pip) and [virtualenv](https://virtualenv.pypa.io)

## Setup

### Get the code
git clone the repo with  the code in a local directory
```bash
https://github.com/Miki-AG/tag_battle.git
```

### Replicate python environment
1. Create virtualenv
```
virtualenv ENV
```

2. Activate the new environment
```
source ./bin/activate
```

3. Move into the tag_battle folder and install all required packages
```
pip install -r requirements.txt
```

### Run manage.py
Move into tag_battle/ht_battle_project/ and run manage.py
```
python manage.py migrate
```

### Create and admin user
```
python manage.py createsuperuser
```

### Startup the dev server
```
python manage.py runserver
```

## Run the application



