from pprint import pprint
from django.urls import reverse
from django.test import Client
from django.test.utils import setup_test_environment

setup_test_environment()

# create an instance of the client for our use
oClient = Client()

# get a response from '/'
response = oClient.get('/')  # Not Found: /
pprint(response.status_code)

# on the other hand we should expect to find something at '/polls/'
# we'll use 'reverse()' rather than a hardcoded URL
response = oClient.get(reverse('polls:index'))
pprint(response.status_code)
pprint(response.content)
pprint(response.context['questions'])  # <QuerySet [<Question: What's up?>]>
