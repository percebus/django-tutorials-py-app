from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get("/hello/{name}")
def hello_name(request, name: str):
    return f"Hello {name}"
