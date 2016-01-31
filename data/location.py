'''
@author: notexit
'''

class Language(object):
    """docstring for Language"""
    def __init__(self, lang):
        #super(Language, self).__init__()
        self.lang = lang

    def language(self):
        if self.lang == "RU":
            return "RU"
        elif self.lang == "EN":
            return "EN"


class Menu(Language):
    """docstring for Menu"""
    def menu(self):
        if self.lang == "RU":
            print("Добро пожаловать")
        elif self.lang == "EN":
            print("Welkome")
