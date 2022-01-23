import random
import time
b = ['Саадат', 'Бакыт', 'Бермет']
print("Это: ",random.choice(b)+'.')
print('Кто лошара? Саадат, Бермет, Бакыт или Данияр?')
a = input('Чтобы узнать нажмите [ENTER].')
if a == '':
    print("Это: ",random.choice(b)+'.')
    
