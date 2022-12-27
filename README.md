# bloghub
write some blogs

clone the repository
```
git clone git@github.com:DGclasher/bloghub.git
```
change to the bloghub directory
```
cd bloghub/
```

install the requirements
```
pip install -r requirements.txt
```

make the required migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

in case of OperationalError
```
python manage.py migrate --run-syncdb
```

run the server
```
python manage.py runserver
```