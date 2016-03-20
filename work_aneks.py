from winsound import PlaySound as play
from winsound import SND_FILENAME as fn
from urllib.request import urlopen as url
from urllib.parse import urlencode as encode
URL = "http://baneks.ru/"
aneks = []

def sound(text):
    t = encode((('text', text), ('format', 'wav'), ('lang', 'ru-RU'), ('speaker', 'zahar'), ('key', '1e0146ea-0b80-425b-8057-fd2feb8ef590')))
    ans = url('https://tts.voicetech.yandex.net/generate?' + t).read()
    f = open('bereza.wav', 'wb')
    f.write(ans)
    play('bereza.wav', fn)
    
for i in range(1, int(input()) + 1):
    html = url(URL + str(i)).read().decode("utf8")
    start = html.find('<meta name="description" content="') + len('<meta name="description" content="')
    end = html.find('<meta name="keywords"') - 7
    aneks.append(html[start:end])
for i in range(0, len(aneks)):
    sound(aneks[i])
