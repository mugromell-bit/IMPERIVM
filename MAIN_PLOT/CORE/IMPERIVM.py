from pathlib import Path
import json
import sys


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
DATA_FILE_PATH = BASE_DIR / "DATA" / "all_chaps_data.json"
with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
    all_chaps_data = json.load(f)



from IMP_ACHIEVES import check_achievements
from IMPERIVM_DEFS import *

from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_I import chapter_1
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_II import chapter_2
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_II_II import chapter_2_2
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_III import chapter_3
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_IIII import chapter_4
from MAIN_PLOT.MAIN_PARTS.PART_I.IMP_CHAP_V import chapter_5
from SIDE_PROJECTS.ROMAN_FISHING import roman_fishing



title("IMPERIVM by VEKCHIS & V-EAGLE")

print("\nСоздано при поддержке:")
title("67 GROUP, PRIME SOVRCE TECH., HAPPY HOLIDAYS CO. & CHEPUHISTIKA INC.")
# print("\nЗадать вопрос, посмотреть код, почитать лор или оставить отзыв об игре можно в нашем телеграм-канале PrimeSovrce")
print("\nТвой путь начинается здесь."
      "\n")
print("ПОСТРОЙ СВОЙ IMPERIVM."
      "\n")
title("ПРОЛОГ")
print("\nТы - один из тысяч мелких правителей во Вселенной. Твои силы невелики, а власть слаба.\n")
print("Твоя цель - Захватить Вселенную."
      "\n")
while True:
    name = input("Твоё имя: ").strip()
    empire_name = input("Название твоего государства: ").strip()
    if name.lower() == "hoffman":
        hoffman_ending()
    if name.lower() == "hara":
        hara_ending()
    if name.lower() == "cibylya":
        cibylya_ending()
    if name.lower() == "роман":
        roman_fishing()
        end()
    if name.lower() == "андрей каренюгин":
        andrei_karenyugin_ending()
    if name.lower() == "андрей каренюгян":
        andrei_karenyugyan_ending()
    if name.lower() == "darvi":
        darvi_ending()
    if empire_name.lower() == "terranova":
        terranova_ending()
    else:
        break

player = Player(name, empire_name)

print(f"\nОтлично, {player.name}, правитель {player.empire_name}.")

#PART I
title("ЧАСТЬ I: 01")
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
