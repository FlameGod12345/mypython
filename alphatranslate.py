#pip install googletrans
#pip install googletrans==3.1.0a0


from googletrans import Translator
b = input('Язык на какой хотите перевести [en, ru]: ')
a = input('Текст: ')
translator = Translator()
c = translator.translate(a, dest=b)
print(c.text)
