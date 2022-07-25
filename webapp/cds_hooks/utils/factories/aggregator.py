import logging
from . import proxy


oLogger = logging.getLogger(__name__)


def create_post(hooks):
    services = {}
    for alias, hook in hooks.items():
        services[alias] = proxy.create_post(hook)

    def post(request):
        responses = {}
        for alias, proxied in services.items():
            responses[alias] = proxied.post(request)

        for response in responses.values():
            response['cards'] += response.json()

        oLogger.info(response)
        return response

    return post
