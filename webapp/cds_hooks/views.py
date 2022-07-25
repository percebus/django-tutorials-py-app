import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt

# from .cds import config
from .cds import client
from .cds import aggregator


# FIXME vvv move to config
config_path = './webapp/cds_hooks/config/cds-hooks.config.json'
with open(config_path, 'r') as oFile:
    json_string = oFile.read()
config = json.loads(json_string)
# FIXME ^^^

groups = config['groups']


@csrf_exempt
def patient_greeting(request):
    hook = groups['patient-view']['hooks']['patient-greeting']
    post = client.create_post(hook)
    proxied = post(request)
    return StreamingHttpResponse(
        proxied.raw,
        status=proxied.status_code,
        reason=proxied.reason,
        content_type=proxied.headers.get('content-type'))


@csrf_exempt
def patient_view(request):
    hooks = groups['patient-view']['hooks']
    post = aggregator.create_post(hooks)
    return post(request)


@csrf_exempt
def order_select(request):
    hooks = groups['order-select']['hooks']
    post = aggregator.create_post(hooks)
    return post(request)
