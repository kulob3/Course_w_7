# tasks.py
from celery import shared_task
import requests

from config.settings import TELEGRAM_TOKEN


@shared_task
def send_telegram_message(chat_id, text):
    token = TELEGRAM_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)