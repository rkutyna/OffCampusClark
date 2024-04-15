# Off Campus Clark

## How To Run

1. Clone this repository

2. Ensure that Docker is installed and running

3. Copy the file dot_env_example to .env (you will also have to create .env)

4. Edit .env and change RANDOM_PASSWORD to a random password and change SOMETHING_LONG_AND_RANDOM to something long and random

5. Run docker compose up -d

6. Run > docker compose exec django python manage.py makemigrations

7. Run > docker compose exec django python manage.py migrate