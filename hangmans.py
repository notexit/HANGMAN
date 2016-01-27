'''
@author: notexit
'''
import sys #импортировал для закрытия программы
import data #импортируем из созданого файла data.py
#импортируем с файла data.py и присвоиваим им имя для удобства
win = data.you_win
lose = data.you_lose
ABC = data.ABC
ABC_RU = data.ABC_RU
menu = data.menu

def restart():
    no[:] = []
    name[:] = []
    start(True)

def start(letter):  #начало игры
    def score(sc):      #функция подсчета балов
        if letter in data.cost_letters:
            sc.append(data.cost_letters[letter])
            if sum(sc) <= 100:
                print("У Вас на счету {0} очков".format(sum(sc)))
                
    word = data.words()
    print("Вам нужно отгадать слово из {0} букв".format(len(word)))
    blanks = "-" * len(word)
    print(blanks)
    while blanks != word:
        blanks = "-" * len(word)
        if bot == [3]:
            letter = data.bot()
        else:
            letter = input("# Введите букву --> ").upper() #предлагается ввод с клавиатуры и записывает ваше значение в letter
        if len(letter) == 1 :   #если длина вашего ввода равна 1
            if letter in ABC_RU:   #если вваш ввод (в данном случае буква) есть в алфавите
                if letter in name:  #если ваша буква есть в списке name
                    if len(name) == 1: #если в списке есть 1 буква
                        print("Эту букву вы уже отгадали : {0} ".format(name))
                    elif len(name) > 1: # если в списке больше чем 1 буква
                        print("Эти буквы вы уже отгадали : {0} ".format(name))
                elif letter in word:    #если вашей буквы нет в списке
                    name.append(letter) #добавляем букву в список
                    score(sc)
                    print(name)     #печатаем букву, которую только что добавили
                elif letter not in word:    #если буквы нет в загаданом слове
                    if letter in no:    #если буквы нет в списке уже вводимых слов
                        if len(no) == 1:    #если длина в списке ровна 1
                            print("Вы уже предлагали такую букву : {0} ".format(no))
                        elif len(no) > 1:   # если больше чем один
                            print("Вы уже предлагали такие буквы: {0} ".format(no))
                    if letter not in no:    #если буквы нет в списке вводимых уже букв
                        no.append(letter)   #добавляем в список вводимые уже буквы
                        errors = len(no) + 1
                        for i in range(1,errors):
                            print(lose[i])
                        if errors == 8:
                            print("Вы проиграли")
                            #print(word)
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
            print("Вы отгадали слово: {0}, поздравляю вы спасли человека".format(word))    #ввывод что вы угадали слово
            sc.append(20)
            print("И получили дополнительно 10 очков, вас счет {0}".format(sum(sc)))
            print(win)
    if sum(sc) >= 100:
        print("У Вас больше 100 очков, Вы победили")
        question = input("Еще раз?  'Д' - что бы сыграть еще раз, или 'ENTER' - для выхода : ")
        if question == "д":      # если мы хотим начать игру с начало, нужно очистить списки
            restart()
        else:
            sys.exit()  #закрывает программу
    else:
        restart()

if __name__ == '__main__':

    menu  #я там сверху его портировал

    name = []       #сюда будут сохранятся буквы, слова
    no = []         #сюда будут сохранятся буквы, которые вы уже ввели
    sc = []
    bot = []

    def input_choice():
        while True:
            choice = input("Ввод:  ")
            if choice == "1":    #если вы выбираете 1, игра начинается
                return start(choice)
            elif choice == "2":
                data.help()
            elif choice == "3":
                bot.append(3)
                return start(choice)
            else:
                print("Я ТАКОЙ КОМАНДЫ НЕ ЗНАЮ")

    choice = input_choice()