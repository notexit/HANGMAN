'''
@author: notexit
'''
from data.location import Menu 

ABC = []

i = input("Choice you language (EN or RU): ").upper()
ABC.append(i)
lan = Menu(i)
print(lan.menu())
print(ABC)