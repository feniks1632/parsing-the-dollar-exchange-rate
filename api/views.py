import logging
import requests


from django.http import JsonResponse

from dollar_parse.settings import API_URL, API_KEY, TRANSLATION_DICT
from .models import UsdRate


def get_current_usd(request):
    """Получает текущий курс USD и сохраняет его в базу данных."""
    try:
        response = requests.get(API_URL, headers={"apikey": API_KEY})
        response.raise_for_status()
        data = response.json()
        current_rate = data["rates"]["RUB"]

        UsdRate.objects.create(rate=current_rate)

        history = UsdRate.objects.all()[:10]

        response_data = {
            'current_rate': current_rate,
            'history': [
                {
                    'timestamp': str(entry.timestamp),
                    'rate': entry.rate
                }
                for entry in history
            ]
        }
        # Переводим данные в русский язык
        response_data = {
            TRANSLATION_DICT.get('current_rate', 'current_rate'): current_rate,
            TRANSLATION_DICT.get('history', 'history'): [
                {
                    TRANSLATION_DICT.get('timestamp', 'timestamp'): str(entry.timestamp),
                    TRANSLATION_DICT.get('rate', 'rate'): entry.rate
                }
                for entry in history
            ]
        }
        logging.info(f'Курс USD обновлен: {current_rate}.')
        return JsonResponse(response_data)
    except requests.exceptions.HTTPError as e:
        logging.error(e)
        return JsonResponse({'error': str(e)})
