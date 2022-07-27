import logging
from django.http import JsonResponse

from . import client


oLogger = logging.getLogger(__name__)


def create_post(hooks):
    services = {}
    for alias, hook in hooks.items():
        services[alias] = client.create_post(hook)

    def _multi_post(request):
        responses = {}
        for alias, post in services.items():
            # TODO try/catch
            response = post(request)
            responses[alias] = response.json()

        cards = []
        for response in responses.values():
            cards += response.get('cards', [])

        body = {'cards': cards}
        oLogger.info(response)
        return JsonResponse(
            body,
            status=200,
            content_type='application/json')

    return _multi_post
