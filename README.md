# `hello-smart-on-fhir-django-py`

Hello SMART-on-FHIR Django py webapp

[![verification](https://github.com/percebus/hello-smart-on-fhir-django-py/actions/workflows/actions.yml/badge.svg)](https://github.com/percebus/hello-smart-on-fhir-django-py/actions/workflows/actions.yml)

## History

See [HISTORY.md](./HISTORY.md)

## `webapp/`

See [`webapp/README.md`](./webapp/README.md)

## Setup

### First time

```bash
$> npm run setup
```

#### FIXME 

Not working: Need to make `source` work from `npm`

### `venv`

```bash
$> python -m venv venv
$> source venv/Scripts/activate
$> npm run setup:ci
```

### Dependencies

```bash
$> npm install
```

## Run

### local

```bash
$> npm start
```

### Docker

```bash
$> npm run start:docker
```

## Browser

```bash
$> npm run browser
```

## Resources

### Django

- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/4.0/intro/tutorial01)

### SMART/FHIR

- [FHIR, SMART, CSD Hooks overview](https://www.youtube.com/watch?v=z5FnHpSxMvs&ab_channel=JoshMandel)
- [SMART FHIR Python Client](http://docs.smarthealthit.org/client-py/)
