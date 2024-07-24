#!/bin/sh

database_inaccessible() {
  export PGPASSWORD=$POSTGRES_PASSWORD
  psql --host=postgres \
    --username=$POSTGRES_USER \
    --dbname=$POSTGRES_DB \
    --command="\dt"
  [ $? -ne 0 ]
  return $?
}

while database_inaccessible ; do
  echo "Waiting for database"
  sleep 2
done

echo "Copying static resources to STATIC_ROOT"
python3 manage.py collectstatic --noinput

echo "Starting Django development server"
#python3 manage.py runserver 0.0.0.0:8000





