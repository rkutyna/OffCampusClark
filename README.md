# Off Campus Clark

## Please explore the website and example listings at http://159.203.179.200

## How To Run

1. Clone this repository

2. Ensure that Docker is installed and running

3. run > cat dot_env_example > .env

4. Edit .env and change RANDOM_PASSWORD to a random password and change SOMETHING_LONG_AND_RANDOM to something long and random

    In .env file set DJANGO_DEBUG=True

5. Run > docker compose up -d

6. Run > docker compose exec django python manage.py migrate

7. Run > docker compose exec django python manage.py createsuperuser

8. You should be able to access the website at localhost:8080




The files/folders nginx, postgres_files, docker, docker-compose.yml, docekrfile, and dot_env_example were taken from https://github.com/ClarkuCSCI/csci220-django

Credit to Dr. Peter Story for these files, our professor for the class this was created, in part, for.


