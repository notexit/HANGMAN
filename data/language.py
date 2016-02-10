'''
@author: notexit
'''

class Language(object):
    """docstring for Language"""
    def __init__(self, lang):
        self.lang = lang

    def language(self):
        if self.lang == "RU":
            return "RU"
        elif self.lang == "EN":
            return "EN"

    def menu(self):
        if self.lang == "RU":
            return("Добро пожаловать")
        elif self.lang == "EN":
            return("Welkome")
