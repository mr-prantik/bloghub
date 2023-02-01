# Contribute to BlogHub

## Steps to perform

+ Fork this repository

+ Clone the dev branch of repo
  ```
  git clone --branch dev git@github.com:[YOUR USERNAME]/bloghub.git
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

+ To run the development server
  ```
  python manage.py runserver
  ```
