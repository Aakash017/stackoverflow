# ASKQuestion
## This is platform where a user can post articles and questions also can like , upvote and answers or comments on other articles/questions.

# Some of the features 

## Login user and maintain session
<img width="1421" alt="Screenshot 2022-09-23 at 4 45 51 PM" src="https://user-images.githubusercontent.com/40654974/191949503-1587e2a0-0d06-4e29-9e75-7b34af19dc3e.png">

## Create a article/question
<img width="1415" alt="Screenshot 2022-09-23 at 4 46 16 PM" src="https://user-images.githubusercontent.com/40654974/191949523-458ee598-72de-445a-8785-24531f968b2a.png">

## Upvote an article/question
<img width="1431" alt="Screenshot 2022-09-23 at 4 46 40 PM" src="https://user-images.githubusercontent.com/40654974/191949529-094cffe6-a6dd-4ad7-91c6-e4919a881c6b.png">


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
