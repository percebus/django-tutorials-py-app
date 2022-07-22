import requests
from django.http import StreamingHttpResponse


def google(request):
    proxied = requests.get('https://google.com', stream=True)
    status = proxied.status_code
    reason = proxied.reason
    content_type = proxied.headers.get('content-type')
    streaming_content = proxied.raw
    return StreamingHttpResponse(
        streaming_content,
        status=status,
        reason=reason,
        content_type=content_type
    )
