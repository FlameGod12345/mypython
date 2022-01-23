from operator import itemgetter

with open('Country_input.txt',encoding="utf8") as file:
    text = file.read()
    text = text.split('\n')
arrayText = list(text)
dText = dict()
#print("arrayText = ",arrayText)

for i in range(len(arrayText)):
    s = arrayText[i].split(';')
    dText.update({s[0]:s[1].strip()})


 for key, value in sorted(dText.items(), key = itemgetter(0), reverse = False):
    listSorted.append(key+";"+value)

f = open('Country_output.txt', "w")
for i in range(len(listSorted)):
    s = listSorted[i].split(';')
    f.write(s[0]+";"+s[1].strip())
    f.write("\n")
f.close()