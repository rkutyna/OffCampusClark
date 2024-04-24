# Off Campus Clark

## How To Run

1. Clone this repository

2. Ensure that Docker is installed and running

3. Copy the file dot_env_example to .env (you will also have to create .env)

4. Edit .env and change RANDOM_PASSWORD to a random password and change SOMETHING_LONG_AND_RANDOM to something long and random

5. Run docker compose up -d

6. Run > docker compose exec django python manage.py makemigrations

7. Run > docker compose exec django python manage.py migrate

## To load image after creating new listing

1. Run docker compose down

2. Run docker compose up -d

The project should show up by going to localhost in a browser.

The files/folders nginx, postgres_files, docker, docker-compose.yml, docekrfile, and dot_env_example were taken from https://github.com/ClarkuCSCI/csci220-django
