'''
@author: notexit
'''
from data.language import Language as lang
from data.help import Help as help



ABC = []

choice = input("Choice you language (EN or RU): ").upper()
ABC.append(choice)
lan = lang(choice)
print(lan.menu())

print(help.help(ABC))

if __name__ == "__main__":

    pass