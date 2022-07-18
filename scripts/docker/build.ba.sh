
# set -x  # DEBUG only
set -v

image='django-tutorials-py-app'
version='latest'
docker build \
  --no-cache \
  --pull \
  --tag "${image}:${version}" \
  --build-arg PGHOST=${PGHOST} \
  --build-arg PGPORT=${PGPORT} \
  --build-arg PGUSER=${PGUSER} \
  --build-arg PGPASSWORD=${PGPASSWORD} \
  --build-arg PGDATABASE=${PGDATABASE} \
  .

set +v
set +x
