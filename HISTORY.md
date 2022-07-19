# `django-tutorials-py-app` 

## HISTORY

### Writing your first Django app

1. `$> django-admin startproject webapp`
1. `$> cd webapp`

#### Part 1

[Writing your first Django app, part 1](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

1. `$> python manage.py startapp polls`

#### Part 2

[Writing your first Django app, part 2](https://docs.djangoproject.com/en/4.0/intro/tutorial02/)

1. `$> python manage.py migrate`

##### `polls_*` tables

1. `$> python manage.py makemigrations polls`
1. `$> python manage.py sqlmigrate polls 0001`
1. `$> python manage.py migrate`

##### super user

1. `$> python manage.py createsuperuser`

#### Part 3

[Writing your first Django app, part 3](https://docs.djangoproject.com/en/4.0/intro/tutorial03/)

1. Added `http(s):polls/{question_id}/*` URLs

#### Part 4

[Writing your first Django app, part 4](https://docs.djangoproject.com/en/4.0/intro/tutorial04/)

1. Added `generic` to `polls/views`

#### Part 5

[Writing your first Django app, part](https://docs.djangoproject.com/en/4.0/intro/tutorial05/)

1. Added Unit Tests
