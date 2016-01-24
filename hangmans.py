'''
@author: notexit
'''
import random
import sys #импортировал для закрытия программы

ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
               "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def words():    
    lis = ["PYTHON", "APPLE", "MICROLAB", "HUMANS", "GREEN", "MICROSOFT", "GITHUB", "FLY", "TABLE"]
    return random.choice(lis)

def start(letter):
    word = words()
    print("Вам нужно отгадать слово из {0} букв".format(len(word)))
    blanks = "*" * len(word)  
    print(blanks)
    while blanks != word:
        blanks = "*" * len(word) 
        live = len(word) - 1
        letter = input("# Введите букву --> ").upper() #предлагается ввод с клавиатуры и записывает ваше значение в letter    
        if len(letter) == 1 :   #если длина вашего ввода равна 1
            if letter in ABC:   #если вваш ввод (в данном случае буква) есть в алфавите
                if letter in name:  #если ваша буква есть в списке name
                    if len(name) == 1: #если в списке есть 1 буква
                        print("Эту букву вы уже отгадали : {0} ".format(name)) 
                    elif len(name) > 1: # если в списке больше чем 1 буква
                        print("Эти буквы вы уже отгадали : {0} ".format(name))
                elif letter in word:    #если вашей буквы нет в списке
                    name.append(letter) #добавляем букву в список
                    print(name)     #печатаем букву, которую только что добавили               
                elif letter not in word:    #если буквы нет в загаданом слове
                    if letter in no:    #если буквы нет в списке уже вводимых слов
                        if len(no) == 1:    #если длина в списке ровна 1
                            print("Вы уже предлагали такую букву : {0} ".format(no))
                        elif len(no) > 1:   # если больше чем один
                            print("Вы уже предлагали такие буквы: {0} ".format(no))      
                    if letter not in no:    #если буквы нет в списке вводимых уже букв
                        no.append(letter)   #добавляем в список вводимые уже буквы     
                        errors = live - len(no)
                        print("Не верно, у вас осталось {0} жизней".format(errors))   
                        if errors == 0:
                            print("Вы проиграли")
                            break
            else:
                print("Я не знаю такого символа")
            for i in range(len(word)):
                if word[i] in name :
                    blanks = blanks[:i] + word[i] + blanks[i + 1:]
            for letter in blanks:
                print (letter, end=' ')
            print ()
        else:
            print("Введите одну букву")
    if blanks == word: #это выполняется, если вы угадали слово
            print("Вы отгадали слово: {0}, поздравляю с победой".format(word))    #ввывод что вы угадали слово
    question = input("Желаете сыграть еще раз? 'y/n' : ")
    if question == "y":      # если мы хотим начать игру с начало, нужно очистить списки
        no[:] = []
        name[:] = []
        start(letter)   #игра начинается с начало
    elif question == "n":
        sys.exit()  #закрывает программу

if __name__ == '__main__': 
    print("""
#######################################################################
#####################Это есть меню...ну, какое есть####################
#######################################################################
#####################       НАЧАТЬ ИГРУ = 1         ###################
###############     выйти с игры = любая другая команда    ############
#######################################################################
"""
    )
    
    name = []       #сюда будут сохранятся буквы, слова
    no = []         #сюда будут сохранятся буквы, которые вы уже ввели

    def input_choice():
        choice = input("Ввод:  ")
        return choice

    choice = input_choice()
    if choice == "1":    #если вы выбираете 1, игра начинается
        start(choice)
    else:
        print("Я ТАКОЙ КОМАНДЫ НЕ ЗНАЮ, ПОКА")