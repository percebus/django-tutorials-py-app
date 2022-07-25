import logging
import requests
from ..security import fhir

oLogger = logging.getLogger(__name__)


def create_post(hook):
    body = {
        'fhirAuthorization': fhir.get_token()
    }

    for param in ['hook', 'hookInstance', 'fhirServer']:
        body[param] = hook[param]

    def post(request):
        for key, value in request.POST.items():
            body[key] = value

        url = hook['url']
        oLogger.info(url)
        oLogger.debug(body)

        return requests.post(url, data=body, stream=False)

    return post
