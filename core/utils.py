import requests
from bs4 import BeautifulSoup


def get_naver_proverb():
    """
    get a korean proverb from naver
    :return: proverb string
    """
    try:
        url = 'http://krdic.naver.com/'
        response = requests.get(url)
        response.encoding = 'utf-8'
        plain_text = response.text
        soup = BeautifulSoup(plain_text, 'html.parser')
    except requests.ConnectionError:
        return '인터넷 연결이 안되어 있습니다. 그래서 오늘의 속담은 없습니다.'
    return soup.select('div > div > dl > dt > a')[2].text

