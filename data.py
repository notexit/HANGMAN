import random

def words():
    lis = ["СНЕГОПАД", "АВТОМОБИЛЬ", "СТУЛ", "ПЕС", "КОТ", "СТОЛ", "НОВОСТИ", "ГЛАЗ", "МИНУС", "ВРАЧ", "КОНЬ"]
    return random.choice(lis)

#будет показывать когда вы проиграли
you_lose = {

    1:    "    #############",
    2:    "        |       #",
    3:    "        O       #",
    4:    "       /|\    / #",
    5:    "       / \   /  #",
    6:    "            /   #",
    7:    "    #############"

}
#покажет что вы выграли вы выграли
you_win = (
"""
           ##############
                 |      #
                 O      #
            \O/       / #
             |       /  #
            / \     /   #
           ##############
"""
)


tex = {  #подсказки для угадованых слов, все слова что в списке, должны быть тут с описом
        "СНЕГОПАД": "Когда идет великое количество снега",
        "АВТОМОБИЛЬ": "Средство предвижения, использует переделаную нафту для передвижения ",
        "СТУЛ": "Помогает сидеть за столом, или одежду складывать",
        "ПЕС": "Верный друг человека",
        "КОТ": "Домашнее животное, мелкий засранец",
        "СТОЛ": "За ним работаю и едят, и комп на нем стоит",
        "НОВОСТИ": "СМИ,вид пропогандической трансляции ",
        "ГЛАЗ": "Вы видите этим мир",
        "МИНУС":"Ниже ноля",
        "ВРАЧ": "Человек, который отдал от 5 до 8 лет жизни для учебы, что бы вас лечить",
        "КОНЬ": "Средство передвижения в старые времена, ща стоит дороже автомобиля "
      }


ABC_RU = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Й", "К", "Л", "М",
               "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ю", "Я", "Ч", "Ь", "Ш", "Щ", "З", "Ъ", "Ы", "Ж", "Э", "И"]

ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
               "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

menu = print("""
#######################################################################
#####################Это есть меню...ну, какое есть####################
#######################################################################
#####################       НАЧАТЬ ИГРУ = 1         ###################
###############     выйти с игры = любая другая команда    ############
#######################################################################
"""
    )

