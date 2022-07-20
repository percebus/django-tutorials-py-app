# `env/` secrets

## Variables

 - `DEBUG`: `(0|1)`

### Django

 - `DJANGO_SECRET_KEY`

### PostgreSQL

I followed the official postgres' [Environment Variables](https://www.postgresql.org/docs/current/libpq-envars.html), (`PG` prefix).

To my surpise, `docker` image `postgres` uses `POSTGRES_` prefix.

 - `PGHOST`
 - `PGPORT`
 - `PGUSER`
 - `PGPASSWORD`
 - `PGDATABASE`

## Setup

1. `$> touch env/localhost.ba.sh`
1. Add needed environment variables
1. `$> source env/localhost.ba.sh`

## Sample

```bash
export DEBUG=1

# SRC: https://www.postgresql.org/docs/current/libpq-envars.html
export PGHOST='localhost'    # FIXME
export PGPORT=5432
export PGUSER='postgres'     # FIXME
export PGPASSWORD='postgres' # FIXME
export PGDATABASE='postgres' # FIXME

export DJANGO_SECRET_KEY='django-VERY-insecure-**********'
```
