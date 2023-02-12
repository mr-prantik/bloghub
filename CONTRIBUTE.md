# Contribute to BlogHub

## Steps to perform

+ Fork this repository

+ Clone the repository
  ```
  git clone git@github.com:[YOUR USERNAME]/bloghub.git
  ```
  
+ Install the requirements
  ```
  pip install -r requirements.txt
  ```

+ Make the required migrations
  ```
  python manage.py makemigrations
  ```
  ```
  python manage.py migrate
  ```
  ```
  python manage.py migrate --run-syncdb
  ```

+ Collect the static files
  ```
  python manage.py collectstatic
  ```

+ To run the development server
  ```
  python manage.py runserver
  ```
