import requests


def get_data(session, Money, url):
    data = requests.get(url).json()
    Money.update(session, data)
