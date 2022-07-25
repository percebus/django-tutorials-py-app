
# set -x  # DEBUG only
set -v

image='django-tutorials-py-app'
version='latest'
docker build \
  --no-cache \
  --pull \
  --tag "${image}:${version}" \
  --build-arg POSTGRES_HOST=${POSTGRES_HOST} \
  --build-arg POSTGRES_PORT=${POSTGRES_PORT} \
  --build-arg POSTGRES_USER=${POSTGRES_USER} \
  --build-arg POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
  --build-arg POSTGRES_DB=${POSTGRES_DB} \
  .

set +v
set +x
