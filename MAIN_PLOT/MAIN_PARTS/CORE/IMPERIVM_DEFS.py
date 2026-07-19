import time


def print_effects(effects):
    effect_texts = []
    for stat, value in effects.items():
        if value > 0:
            effect_texts.append(f"+{value} {stat}")
        else:
            effect_texts.append(f"{value} {stat}")

    print("Эффекты: " + ", ".join(effect_texts))



class Player:
    def __init__(self, name, empire_name):
        self.name = name
        self.empire_name = empire_name
        self.honor = 10
        self.authority = 10
        self.economy = 10
        self.diplomacy = 0
        self.propaganda = 0
        self.espionage = 0
        self.fear = 0
        self.science = 10
        self.supply = 10
        self.armament = 10
        self.army_size = 500_000_000
        self.honor_crisis = 0
        self.authority_crisis = 0
        self.unlocked_achievements = set()
        self.dark_knights_alliance = False
        self.lima_alive = False
        self.robert_whitemann = False
        self.adam_kreuz_accept = False
        self.adam_kreuz_read_letter = False
        self.dum_death = False
    @property
    def fight_spirit(self):
            return (self.propaganda + self.authority) * 0.5

    @property
    def army_power(self):
            return (self.fight_spirit + self.supply + self.economy + self.authority +
                    self.armament) * 0.2 + self.army_size // 20_000_000

    @property
    def stability(self):
            return (self.authority + self.economy + self.espionage + self.fear) * 0.23

    def end_turn(self):
        # Обновляем счётчики
        if self.honor <= 0:
            self.honor_crisis += 1
        else:
            self.honor_crisis = 0

        if self.authority <= 0:
            self.authority_crisis += 1
        else:
            self.authority_crisis = 0

        # Применяем последствия
        if self.honor_crisis >= 3:
            self.authority -= 1
            print("⚠ Из-за низкой чести начал падать авторитет!")

        if self.authority_crisis >= 3:
            self.economy -= 1
            print("⚠ Из-за низкого авторитета начала падать стабильность!")

        # Сообщения о текущем состоянии (только если кризис активен)
        if self.honor <= 0 or self.authority <= 0:
            print(f"АКТИВЕН КРИЗИС. ТЕКУЩИЕ ПАРАМЕТРЫ:   Честь: {self.honor} | Авторитет: {self.authority} | "
                  f"Стабильность: {self.stability:.1f}")
#Запретные имена и империи
forbidden_names = {"ант", "д", "дд", "цезарь", "чех", "ром iii", "ром 3", "хеффман", "эмилио", "марк"}
forbidden_empires = {"пятый рим", "третий рейх", "true human rebellion", "thl", "мона", "империя мона"}



def apply_and_show_effects(player, event):
    print("\n" + "─" * 50)
    print("ПРИМЕНЯЕМ ЭФФЕКТЫ:")

    changed_stats = {}

    for stat, value in event["effects"].items():
        if hasattr(player, stat) and stat != "stability":  # не показываем стабильность
            old = getattr(player, stat)
            new = old + value
            setattr(player, stat, new)

            changed_stats[stat] = (old, new, value)

            sign = "+" if value > 0 else ""
            print(f"  {stat.capitalize():12} {old:4} → {new:4} ({sign}{value})")
    if player.honor <= 0:
        print("Твоя честь упала до нуля! Подними её, иначе с каждым ходом твой авторитет будет падать.")
    if player.authority <= 0:
        print("Твой авторитет упал до нуля! Подними его, иначе с каждым ходом стабильность будет падать.")

    player.end_turn()
    print("─" * 50)


def choose_event(events_dict, category_name):
    print(f"\nТы можешь повлиять на {category_name} тремя способами:")

    for num, event in events_dict.items():
        print(f"\n{num} — {event['name']}")
        print(f"Описание: {event['desc']}")
        print_effects(event['effects'])

        # --- ДОБАВЛЯЕМ ПРОВЕРКУ РИСКОВ ДЛЯ ВТОРОЙ ГЛАВЫ ---
        if "risk_chance" in event:
            risk_percent = int(event["risk_chance"] * 100)
            # Забираем штраф к дипломатии (если его нет в risk_effect, вернет 0)
            diplomacy_penalty = event["risk_effect"].get("diplomacy", 0)
            print(f"Шанс провала ({risk_percent}%): {diplomacy_penalty} Дипломатия")

        if "war_chance" in event:
            war_percent = int(event["war_chance"] * 100)
            print(f"Критический риск/ Война ({war_percent}%)")
        # --------------------------------------------------

    while True:
        try:
            choice = (input(f"\nВведи номер способа (1-3): ")).strip()
            if choice in events_dict:
                selected_event = events_dict[choice]
                print(f"\nТы выбрал способ {selected_event['name']}!")
                return selected_event  # возвращаем выбранное событие
            else:
                print("Выбери число от 1 до 3.")
        except ValueError:
            print("Введи число!")
#---------------------------------------------------

#ВЫВОД ТЕКСТА
def say(text, delay=0.02, end="\n"):
    """Красиво выводит текст в игре"""
    for char in str(text):
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end=end)


def separator(length=60):
    print("=" * length)


def title(text):
    separator(70)
    print(f"{' ' * 10}{text.center(50)}")
    separator(70)

def end():
    say("\n=== ИГРА ОКОНЧЕНА ===", delay=0.05)
    input("\nНажми Enter, чтобы выйти...")
    exit()


def war():
    input("Нажми Enter, чтобы начать новую главу"
          "\n ")
    title("ВОЙНА")
    print("Идёт война", end="")
    for _ in range(5):  # 5 точек
        print(".", end="", flush=True)
        time.sleep(0.6)
    print()


def new_chap():
    input("Нажми Enter, чтобы начать новую главу"
          "\n")
