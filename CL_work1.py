with open('Country_input.txt', encoding="utf8") as file:
    text = file.read()
    text = text.replace('\n', ', ')
print(text)

print('Dict of the text')
d = {}
d = dict(d.split(';'))
for d in text.split(','):
    print(d)

print('Method of the dict - items')
for key, value in d.items():
    print(key, '-', value)

list_keys = list(d.keys())
list_keys.sort()

for key in list_keys:
    print(key, '-', d[key])

new_file = open('Country.output.txt', 'w+')
new_file.write(list_keys)
