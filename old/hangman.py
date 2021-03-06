'''
@author: notexit
'''
import random           #импортирую для случайного выбора слова из списка

# алфавиты, добавил не знаю зачем, может потом усовершенствую игру
ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
       "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

ABC_RU = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л",
       "М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш",
       "Щ","Ъ","Ы","Ь","Э","Ю","Я"]
# приветствие в начале игры
print("""
    ##################################################
    ##############     ПРИВЕТСТВУЮ      ##############
    ##################################################
    
                    ИГРА НАЧАЛАСЬ
    """
)

lis = ["PYTHON", "APPLE", "MICROLAB", "HUMANS", "GREEN", "MICROSOFT", "GITHUB", "FLY", "TABLE"] #это список слов, которые будут угадывать

word = random.choice(lis) #выбирает случайное слово из списка

live = len(word) - 1 #это есть жизни, их количество равно длине слова минус 1

name = []       #сюда будут сохранятся буквы, слова
no = []         #сюда будут сохранятся буквы, которые вы уже ввели
blanks = "*" * len(word)    #используем для скрытия слов 

print("Вам нужно отгадать слово из {0} букв".format(len(word))) #показывает сообщение, сколько вам нужно угадать букв

while blanks != word: #начинаем цыкл, он будет продолжатся до того времени, пока вы не угадаете слово
        
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
                        #input("Press Enter")
                        break
                
        elif letter in ABC_RU:  #если вводимая буква есть в русском алфавите
            print("Не правильная кодировка")    #печатаем 
        
        #этот блок нужен для того, что бы скрывать угаданое слово, и показывать уже угаданые буквы
        for i in range(len(word)):
            if word[i] in name :
                blanks = blanks[:i] + word[i] + blanks[i + 1:]
        for letter in blanks:
            print (letter, end=' ')
        print ()       
                
    else:     #если вы не ввели  букву или ввели больше чем одну
        print("Введите одну букву")

if __name__ == '__main__':
    
    if blanks == word: #это выполняется, если вы угадали слово
        print("Вы отгадали слово: {0}, поздравляю с победой".format(word))    #ввывод что вы угадали слово
        #input("Press Enter")
        