These files are:

See [Creating a project](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#creating-a-project)

# `webapp/`

The outer `mysite/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

## `manage.py`

A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

## `webapp/`

The inner `mysite/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

### `__init__.py`

`mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.


### `settings.py`

`mysite/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

### `urls.py`

`mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

### `asgi.py`

`mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.

### `wsgi.py`

`mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.
