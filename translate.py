import requests 
 
def get_translation(text,lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
    KEY = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97' 
    TEXT = text
    LANG = lang
    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return eval(r.text)
 
print(*get_translation(input(':>'),'en')['text'])
