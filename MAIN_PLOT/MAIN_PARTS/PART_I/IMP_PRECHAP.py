import json
import os

# Находит папку IMPERIVM и строит путь к DATA
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ideologies_path = os.path.join(BASE_DIR, "DATA", "../DATA/ideologies.json")
philosophies_path = os.path.join(BASE_DIR, "DATA", "../DATA/philosophies.json")

# Загрузка данных в переменные для импорта
with open(ideologies_path, "r", encoding="utf-8") as f:
    ideologies = json.load(f)

with open(philosophies_path, "r", encoding="utf-8") as f:
    philosophies = json.load(f)



