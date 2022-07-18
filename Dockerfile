FROM nikolaik/python-nodejs:python3.10-nodejs16

# TODO? or XXX?
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

ARG PGHOST='localhost'
ARG PGPORT=5432
ARG PGUSER
ARG PGPASSWORD
ARG PGDATABASE='tutorials'

ENV PGHOST ${PGHOST}
ENV PGPORT ${PGPORT}
ENV PGUSER ${PGUSER}
ENV PGPASSWORD ${PGPASSWORD}
ENV PGDATABASE ${PGDATABASE}

WORKDIR /code
COPY . .
# RUN sed -i 's/\r$//' ./scripts/**/*.sh
RUN ls -la
RUN npm run setup:ci && npm ci
RUN npm test

EXPOSE 8000
# RUN ["python", "webapp/manage.py", "migrate"]  # TODO

ENTRYPOINT ["python", "webapp/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
