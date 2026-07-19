#IMPERIVM.py
from pathlib import Path
import json
import sys


# 1. Находим корень вашего проекта (папку IMPERIVM) относительно этого файла
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Добавляем корень в пути для импортов (замена вашей строки 6)
sys.path.append(str(BASE_DIR))

# 3. Формируем точный путь к файлу в папке DATA
DATA_FILE_PATH = BASE_DIR / "DATA" / "all_chaps_data.json"

# 4. Открываем файл по точному пути
with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
    all_chaps_data = json.load(f)

from IMP_ACHIEVES import check_achievements
from IMPERIVM_DEFS import *

from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_PRECHAP import philosophies, ideologies
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_I import chapter_1
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_II import chapter_2
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_II_II import chapter_2_2
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_III import chapter_3
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_IIII import chapter_4
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_V import chapter_5
from MAIN_PLOT.MAIN_PARTS.PART_I.CHAPTER_VI import chapter_6


print("Добро пожаловать в The Game/ PythonProject5.")
title("MADE BY VEKCHIS & PRIME SOURCE GROUP")
print("Задать вопрос, посмотреть код, почитать лор или оставить отзыв о игре можно на нашем сайте PrimeSource.ru")
print("Твой путь начинается здесь.")
title("ЧАСТЬ I: NO CHURCH IN THE WILD")
print("Ты - один из тысяч мелких правителей во Вселенной. Твои силы невелики, а власть слаба.\n")
print("Твоя цель - захватить Вселенную.")
print("ПОСТРОЙ СВОЙ IMPERIVM.")
while True:
    name = input("Твоё имя: ").strip()
    empire_name = input("Название твоего государства: ").strip()
    if name.lower() == "хоффман":
        title("ГЕНИАЛЬНАЯ ПОБЕДА")
        print("Используя законы физики, ты создаёшь атомный дезинтегратор и уничтожаешь противников!")
        exit()
    if name.lower() == "андрей":
        title("ЛОГИЧЕСКАЯ ПОБЕДА")
        print("Используя программируемую армию роботов, ты становишься абсолютным правителем Вселенной!")
        exit()
    if name.lower() == "андрей хоффман":
        title("АБСОЛЮТНАЯ ПОБЕДА")
        print("Используя самообучающихся роботизированных солдат ты не оставляешь шансов врагам своего государства!")
        exit()
    if name.lower() in forbidden_names:
        print("Это имя занято, попробуй другое.")
        continue
    if empire_name.lower() in forbidden_empires:
        print("Такая Империя уже существует, будь уникальнее.")
        continue
    else:
        break

player = Player(name, empire_name)

print(f"\nОтлично, {player.name}, правитель {player.empire_name}.")

print("Первое - идеология. От неё зависит с кем ты станешь союзником, врагом и какие фокусы сможешь проводить.")
print("Выбери идеологию своего государства:")
for num, ideo in ideologies.items():
    print(f"\n{num} — {ideo['name']}")
    print(f"Описание: {ideo['desc']}")
    print(f"Плюсы: {ideo['advantages']}")
    print(f"Минусы: {ideo['disadvantages']}")
    print(f"Стиль игры: {ideo['style']}")
    print(f"Уровень сложности: {ideo['difficulty']}")
while True:
    try:
        choice = (input("\nВведи номер идеологии (1-5): "))
        if choice in ideologies:
            ideology = ideologies[choice]
            print(f"\nТы выбрал идеологию {ideology['name']}!")
            break
        else:
            print("Выбери число от 1 до 5.")
    except ValueError:
        print("Введи число!")
print("Так как ты человек, у тебя есть своя философия.")
print("Выбери свою философию:")
for num, phil in philosophies.items():
    print(f"\n{num} — {phil['name']}")
    print(f"Описание: {phil['desc']}")
    print(f"Плюсы: {phil['advantages']}")
    print(f"Минусы: {phil['disadvantages']}")
    print(f"Стиль игры: {phil['style']}")
    print(f"Уровень сложности: {phil['difficulty']}")
while True:
    try:
        choice = (input("\nВведи номер философии (1-4): "))
        if choice in philosophies:
            philosophy = philosophies[choice]
            print(f"\nТы выбрал философию {philosophy['name']}!")
            break
        else:
            print("Выбери число от 1 до 4.")
    except ValueError:
        print("Введи число!")



#MAIN PLOT

#CHAPTER I
player = chapter_1(player, all_chaps_data["chapter 1"])
new = check_achievements(player)
if new:
    player.unlocked_achievements.update(new)

#CHAPTER II
player = chapter_2(player, all_chaps_data["chapter 2"])
new = check_achievements(player)
if new:
    player.unlocked_achievements.update(new)

#CHAPTER II, PART II
if player.diplomacy <= -10:
    player = chapter_2_2(player, all_chaps_data["chapter 2_2"])
    new = check_achievements(player)
    if new:
        player.unlocked_achievements.update(new)

#CHAPTER III
player = chapter_3(player)
new = check_achievements(player)
if new:
    player.unlocked_achievements.update(new)

#CHAPTER IIII
player = chapter_4(player, all_chaps_data["chapter 4"])
new = check_achievements(player)
if new:
    player.unlocked_achievements.update(new)

#CHAPTER V
player = chapter_5(player, all_chaps_data["chapter 5"])
new = check_achievements(player)
if new:
    player.unlocked_achievements.update(new)

#CHPATER VI
player = chapter_6(player)
