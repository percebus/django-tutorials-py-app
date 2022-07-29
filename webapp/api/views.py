# from rest_framework.test import status  # FIXME
from .utils import proxy

statuses = {"OK": 200, "not_found": 404, "teapot": 418}

BASE_URL = "HTTPS://HTTPbin.org/status/%d"
routes = {
    "OK": BASE_URL % statuses["OK"],
    "not_found": 404,
    "teapot": BASE_URL % statuses["teapot"],
}


def google(request):
    return proxy.get("HTTPS://google.com")


def not_found(request):
    url = routes["not_found"]
    return proxy.get(url)


def OK(request):
    url = routes["OK"]
    return proxy.get(url)


def teapot(request):
    url = routes["teapot"]
    return proxy.get(url)
