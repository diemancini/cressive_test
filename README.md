### INSTALATION

In order to run this aplication, you have to follow these steps bellow:

### 1 - Install docker and docker compose (https://docs.docker.com/compose/)

### 2 - Run 
```bash
    docker-compose up web
```
for building and running the application automatically.

### 3 - After ran the command above, you need to setup the application with:

#### 3.1 - Migrations:
```bash
    docker-compose run web python manage.py migrate
```
#### 3.2 - Create a user:
```bash
    docker-compose run web python manage.py shell
```
After the command above, you should see a new shell terminal and insert this script bellow:

```python
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
    u = user_model.objects.create_superuser(
        username="diego.mancini",
        email="diego.mancini@admin.com",
        password="123456"
    )
    exit()
```

#### 3.3 - Create a token for the user:
```bash
docker-compose run python manage.py drf_create_token {username}
```
    Copy the generated token that appeared in terminal and paste in API_TOKEN variable in env_files/local

#### 3.4 - Run the application with cron:

    Stop the application (if is running) with ctrl+C, open docker-compose.yml file and comment the line 8, where shows:
```bash
    command: sh -c "python manage.py runserver 0.0.0.0:8000"
```
    And uncomment the line 9:
```bash
    #entrypoint: sh ./docker-entrypoint.sh
```
    Change the permissions of docker-entrypoint.sh with:
```bash
    sudo chmod +x path/to/the/file/docker-entrypoint.sh
```
    Run docker-compose up web again and now you should see in terminal:
```bash
    adding cronjob: (9c3bf040ae97b75c381704b21865e5c7) -> ('0 0 * * *', 'scraping.cron.start_scraping', '>> /cron/django_cron.log')
```
    If you want to change the date of the endpoint that will trigger the scrapping, just opent cressive_test/settings/local file.

## Application

Access the admin mode in this project :
```bash
    http://localhost:8000/admin
```  
    You should see login page and use the credentials (username and password) that you created in (3.2) of 'Instalation'.
#### Creating the keywords:
    After logged, just click in keyword>add keywords and create a new word for the scraping search in the scheduled time.

#### Sponsored and Organic results:
    The scraping is able to separate the results between them. Each one will be saved in Sponsored and Organic models. You 
can see the list for each model in admin page.
#### Trigger the scraping:
    This will be triggered by endpoint:
```bash
    /api/v1/scraping/start
```    
    Where this automatically activate the scraping script, which will still running in background after the response of endpoint.
    The endpoint will be triggered by a crontab app, filtered the keywords by the date that word was created.


## Issues and Improvements

### Issues

The application has some issues that needs to be improved, such as:

* In the 'description' field it was not possible to get the data efficiently. So this field will be filled out as empty, but the code is in there (line 98, in scraping/scraping.py)
* Sometimes, you possibly see this error in logs when you try to re-run this application: 
```bash
    RuntimeError: No job with hash 9c3bf040ae97b75c381704b21865e5c7 found. It seems the crontab is out of sync with your settings.CRONJOBS. Run "python manage.py crontab add" again to resolve this issue!
```
    If that happens, just re-run 'docker-compose up web' again.

### Improvements

* Amazon has some tricky fields to get. So probably with another library could be different (scrapy or BeautifulSoup)
* 
    
