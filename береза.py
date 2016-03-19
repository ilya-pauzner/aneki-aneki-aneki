from winsound import PlaySound as play
from winsound import SND_FILENAME as fn
from urllib.request import urlopen as url
from urllib.parse import urlencode as encode

def sound(text):
    t = encode((('text', text), ('format', 'wav'), ('lang', 'ru-RU'), ('speaker', 'zahar'), ('key', '1e0146ea-0b80-425b-8057-fd2feb8ef590')))
    ans = url('https://tts.voicetech.yandex.net/generate?' + t).read()
    f = open('bereza.wav', 'wb')
    f.write(ans)
    play('bereza.wav', fn)

text = 'Абракадабра зеленая швабра'
sound(text)