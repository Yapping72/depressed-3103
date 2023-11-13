#!/bin/sh
set -e

# Function to check if the PostgreSQL server is available
is_pg_ready() {
    PGPASSWORD=${POSTGRES_PASSWORD} pg_isready -h basic_web_db -U ${POSTGRES_USER}
}

# Function to check if the database exists
db_exists() {
    PGPASSWORD=${POSTGRES_PASSWORD} psql -h basic_web_db -U "${POSTGRES_USER}" -tc "SELECT 1 FROM pg_database WHERE datname = '${POSTGRES_DB_NAME}';" | grep -q 1
}

# Wait for the PostgreSQL server to become available
until is_pg_ready; do
    echo "Waiting for database to become available..."
    sleep 2
done

# Create the database if it doesn't exist
if ! db_exists; then
    echo "Creating database..."
    PGPASSWORD=${POSTGRES_PASSWORD} psql -h basic_web_db -U "${POSTGRES_USER}" -c "CREATE DATABASE ${POSTGRES_DB_NAME}"
fi


# Apply database migrations
echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
exec "$@"
