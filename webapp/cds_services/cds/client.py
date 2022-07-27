import json
import logging
import requests


oLogger = logging.getLogger(__name__)


def parse(request):
    json_string = request.body.decode('utf-8')
    return json.loads(json_string)


def create_post(hook):
    data = {}

    for param in ['hook', 'hookInstance', 'fhirServer']:
        data[param] = hook[param]

    def _post(request):
        oLogger.error(request)

        body = parse(request)
        for key, value in body.items():
            data[key] = value

        url = hook['url']
        oLogger.info(url)
        oLogger.debug(data)

        return requests.post(url, json=data, stream=True)

    return _post
