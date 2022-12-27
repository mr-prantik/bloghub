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
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

run the server
```
python3 manage.py runserver
```