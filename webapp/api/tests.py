from django.urls import reverse
from django.test import TestCase


class HttpBinApiUrlsTests(TestCase):
    def test_OK(self):
        response = self.client.get(reverse('api:OK'))
        self.assertEquals(response.status_code, 200)

    def test_teapot(self):
        response = self.client.get(reverse('api:teapot'))
        self.assertEquals(response.status_code, 418)

    def test_not_found(self):
        response = self.client.get(reverse('api:not_found'))
        self.assertEquals(response.status_code, 404)


class GoogleApiUrlsTests(TestCase):
    def test_google(self):
        response = self.client.get(reverse('api:google'))
        self.assertEquals(response.status_code, 200)
