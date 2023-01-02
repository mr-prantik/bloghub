# bloghub
write some blogs

django application to write blogs

install the requirements
```
pip install -r requirements.txt
```

make the required migrations
```
python manage.py makemigrations blog users
```
```
python manage.py migrate
```
```
python manage.py migrate --run-syncdb
```

run the server
```
python manage.py runserver
```