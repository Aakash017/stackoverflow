# ASKQuestion
## This is platform where a user can post articles and questions also can like , upvote and answers or comments on other articles/questions.

# Some of the features 
## login user and maintain session
## Create a article/question
## Answer on article/question
## Upvote an article/question
## Upvote Comment on article/question


Steps:
git clone https://github.com/Aakash017/stackoverflow.git

create new virtaulenv and activate the same
```python
python3.7 -m virtualenv <env_name>
```

```python
source <env_name>/bin/activate/
```

create new database and update database sesstings in sesstings.py

```sql
create database <db_name>;
```

# Edit Settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'db_name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

## Now you are good to go

# Start your server

```python
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
