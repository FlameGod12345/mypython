#def bebra(name = 'Name'):
#   print('Hello ' + name)
#bebra(5)

def sum_of_two_numbers(a = 0, b = 0):
    return a + b
a = int(input())
b = int(input())
x = sum_of_two_numbers(a, b)
#x = sum_of_two_numbers()
print(x)

def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False
print(is_hello_in_text('Say Hello everyone'))

def beb(a):
    return 'hello' in a.lower()
print(beb('everyone'))

def huk(st, te):
    return st in te
print(huk('he', 'hehehe'))
