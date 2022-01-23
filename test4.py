import re
a = input()
b = list(a)
for i in range(len(b)):
    if (re.search("[0-9]", b[i])):
       print(b[i])
for i in range(len(b)): 
    if (re.search("[^0-9]", b[i])):
       print(b[i])

def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(78)
