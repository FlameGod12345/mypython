from operator import itemgetter

d = {"aa": 3, "bb": 4, "cc": 2, "dd": 1}
listSorted = []
i=0
for key, value in sorted(d.items(), key = itemgetter(0), reverse = False):
    print(key, value)
    i=i+1
    listSorted.append(key+";"+str(value))

print("listSorted = ", listSorted)