#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    CREATE USER '$PGUSER' WITH PASSWORD '$PGPASSWORD';
    ALTER USER '$PGUSER' WITH SUPERUSER;
    CREATE DATABASE '$DATABASE_NAME';
    GRANT ALL PRIVILEGES ON DATABASE postgres TO '$PGUSER';
EOSQL
echo "Done! Creating DB"