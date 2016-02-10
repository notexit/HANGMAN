class Help(object):
    """This help this game"""
    def __init__(self,ABC):
        self.ABC = ABC

    def help(self):
        if self.ABC == "RU":
            return("""
            Все ваши действия вы должны подтверждать нажатием кнопки 'ENTER'
            Вы вводите букву, которая на ваш взгляд есть у слове,
            и нажимаете 'ENTER', всю осталюную информацию будут показывать подсказки
            """)
        elif self.ABC == "EN":
            return("""
            All your actions, you must confirm by pressing 'ENTER' button
            You enter the letter that you think have a word,
            and press 'ENTER', all the information will show ostalyunuyu tips
            """)