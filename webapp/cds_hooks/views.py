
from django.views.decorators.csrf import csrf_exempt

from .utils.cds import config
from .utils.factories import proxy
from .utils.factories import aggregator


hooks = config['hooks']

@csrf_exempt
def patient_greeting(request):
    hook = hooks['patient-view']['services']['patient-greeting']
    proxied_post = proxy.create_post(hook)
    return proxied_post(request)


@csrf_exempt
def patient_view(request):
    _hooks = hooks['patient-view']
    aggregated_post = aggregator.create_post(_hooks)
    return aggregated_post(request)


@csrf_exempt
def order_select(request):
    _hooks = hooks['order-select']
    aggregated_post = aggregator.create_post(_hooks)
    return aggregated_post(request)
