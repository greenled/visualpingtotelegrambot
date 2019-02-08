from django.http import HttpResponse
from django.conf import settings
import json
import requests


message_template = """
{preview}
We detected a change of <b>{change}</b> on <b>{description}</b>.
Change detected on <i>{datetime}</i>.
See {url} for details.
"""


def send_message_to_telegram_bot(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        payload = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'parse_mode': 'HTML',
            'text': message_template.format(
                url=body['url'],
                description=body['description'],
                datetime=body['datetime'],
                preview=body['preview'].replace('/home/rdudler/sites/', ''),
                change=body['change']
            )
        }
        r = requests.get(
            'https://api.telegram.org/bot{token}/sendMessage'
            .format(token=settings.TELEGRAM_BOT_TOKEN), params=payload)
        return HttpResponse("ok")
    return HttpResponse("use POST")
