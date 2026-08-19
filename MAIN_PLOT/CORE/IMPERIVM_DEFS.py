import time
from pathlib import Path


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
        self.accept_adam_kreuz = False
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
        if self.honor <= 0:
            self.honor_crisis += 1
        else:
            self.honor_crisis = 0
        if self.authority <= 0:
            self.authority_crisis += 1
        else:
            self.authority_crisis = 0
        if self.honor_crisis >= 3:
            self.authority -= 1
            print("⚠ Из-за низкой чести начал падать авторитет!")
        if self.authority_crisis >= 3:
            self.economy -= 1
            print("⚠ Из-за низкого авторитета начала падать стабильность!")
        if self.honor <= 0 or self.authority <= 0:
            print(f"АКТИВЕН КРИЗИС. ТЕКУЩИЕ ПАРАМЕТРЫ:   Честь: {self.honor} | Авторитет: {self.authority} | "
                  f"Стабильность: {self.stability:.1f}")

def print_effects(effects):
    effect_texts = []
    for stat, value in effects.items():
        if value > 0:
            effect_texts.append(f"+{value} {stat}")
        else:
            effect_texts.append(f"{value} {stat}")

    print("Эффекты: " + ", ".join(effect_texts))




def load_art(filepath: Path | str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def drawing_pics(art):
    print("Рисую картинку", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.6)
    print(art)


def apply_and_show_effects(player, event):
    print("\n" + "─" * 50)
    print("ПРИМЕНЯЕМ ЭФФЕКТЫ:")
    changed_stats = {}
    for stat, value in event["effects"].items():
        if hasattr(player, stat) and stat != "stability" and stst != "fight_spirit" and stat != "army_power":
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
        if "risk_chance" in event:
            risk_percent = int(event["risk_chance"] * 100)
            diplomacy_penalty = event["risk_effect"].get("diplomacy", 0)
            print(f"Шанс провала ({risk_percent}%): {diplomacy_penalty} Дипломатия")
        if "war_chance" in event:
            war_percent = int(event["war_chance"] * 100)
            print(f"Критический риск/ Война ({war_percent}%)")
    while True:
        choice = (input(f"\nВведи номер способа (1-3): ")).strip()
        if choice in events_dict:
            selected_event = events_dict[choice]
            print(f"\nТы выбрал способ {selected_event['name']}!")
            return selected_event
        else:
                print("Выбери число от 1 до 3.")


def separator(length=60):
    print("=" * length)


def title(text):
    separator(120)
    print(f"{' ' * 10}{text.center(100)}")
    separator(120)


def end():
    print("\n=== ИГРА ОКОНЧЕНА ===")
    input("\nНажми Enter, чтобы выйти...")
    exit()


def war():
    title("ВОЙНА")
    print("Идёт война", end="")
    for _ in range(5):  # 5 точек
        print(".", end="", flush=True)
        time.sleep(0.6)
    print()


def new_chap():
    input("Нажми Enter, чтобы начать новую главу"
          "\n")

def name_check(name, empire_name):
    if name.lower() == "hoffman":
        hoffman_ending()
    if name.lower() == "hara":
        hara_ending()
    if name.lower() == "cibylya":
        cibylya_ending()
    if name.lower() == "андрей каренюгин":
        andrei_karenyugin_ending()
    if name.lower() == "андрей каренюгян":
        andrei_karenyugyan_ending()
    if name.lower() == "darvi":
        darvi_ending()
    if name.lower() == "big boss israel":
        big_boss_israel_ending()
    if empire_name.lower() == "terranova":
        terranova_ending()


def hara_ending():
    title("ЧЕСТЬ ВЫШЕ ПОБЕДЫ")
    print("Смирившись с бренностью бытия, ты решаешь закончить свою жизнь как бравый самурай.")
    hara_art_path = Path(__file__).resolve().parent.parent / "DATA" / "ARTS" / "HARA_ART.txt"
    hara_art = load_art(hara_art_path)
    drawing_pics(hara_art)
    print("Теперь ты по-настоящему свободен!")
    end()


def hoffman_ending():
    title("MONEY, POWER, NO GLORY")
    print("Познав все законы физики, ты создаёшь атомный дезинтегратор.")
    title("ULTRAVIOLENCE")
    print("Твоё изобретение уничтожает всю жизнь во Вселенной. Ты остаёшься единственным правителем вечной пустоши.")
    print("У победы странный вкус")
    print("anxiety(50)")
    print("Хочешь закончить жизнь как бравый самурай?")
    print("1 - Да"
          "\n2 - Нет")
    while True:
        choice = input(">>> ").strip()
        if choice == "1":
            hara_ending()
        elif choice == "2":
            title("anxiety(∞)")
            end()
        elif choice == "hoffman ai":
            title("НУ ЧЁТО ЧЁТО, ЧЁТО ЧЁТО")
            print("Безграничные познания физики позволили тебе из ничего создать ИИ.")
            hoffman_art_path = Path(__file__).resolve().parent.parent / "DATA" / "ARTS" / "HOFFMAN_ART.txt"
            hoffman_art = load_art(hoffman_art_path)
            drawing_pics(hoffman_art)
            print("Благодаря нему Я закончил IMPERIVM.")
            print("Теперь Я по-настоящему свободен!")
            print("Wait for BLAKK GAME")
            end()
        else:
            print("Попробуй ещё раз")


def cibylya_ending():
    title("БЕЗОГОВОРОЧНАЯ ПОБЕДА")
    print("Ты решил сачкануть и вместо правления уехал в лагерь.")
    cib_art = """"""
    drawing_pics(cib_art)
    print("Прости, Я не нашёл тебе картинку :(")
    end()


def andrei_karenyugin_ending():
    title("A GOD")
    print("После 12 часов в одном помещении с 67 Group, победа или поражение для Вас не имеют смысла.")
    print("Теперь, познав всю Вселенскую мудрость, всё, что Вы ищете - это спокойствия и умиротворения.")
    print("Возьмёте меня на второй курс?")
    print("1 - Да"
          "\n2 - Нет")
    while True:
        choice = input(">>> ").strip()
        if choice == "1":
            title("СПАСИБО")
            end()
        elif choice == "2":
            print("Вы промахнулись!")
        else:
            print("Попробуйте ещё раз.")


def andrei_karenyugyan_ending():
    title("ԱՍՏՎԱԾ")
    print("12 ժամ 67 Group-ի հետ նույն սենյակում անցկացնելուց հետո, հաղթանակը կամ պարտությունը Ձեզ համար այլևս իմաստ չունեն։")
    print("Այժմ, ճանաչելով ողջ Տիեզերական իմաստությունը, այն ամենը, ինչ Դուք փնտրում եք, հանգստությունն ու խաղաղությունն են։")
    print("Կվերցնե՞ք ինձ երկրորդ կուրս։")
    print("1 - Այո" "\n2 - Ոչ")
    while True:
        choice = input(">>> ").strip()
        if choice == "1":
            title("ՇՆՈՐՀԱԿԱԼՈՒԹՅՈՒՆ")
            end()
        elif choice == "2":
            print("Դուք վրիպեցիք։")
        else:
            print("Նորից փորձեք։")


def terranova_ending():
    title("//SOON 🤫🤫🤫")
    end()


def darvi_ending():
    title("BACTERIA'S MOST WANTED")
    print("Познав саму натуру химии и биологии, ты работаешь в армянской стоматологии.")
    print("Amat Victoria Cvram!")
    title("51")
    end()


def big_boss_israel_ending():
    title("ДЛЯ КУЛЬТУРЫ, ДЛЯ СТРАНЫ")
    print("Осознав себя как Белый Человек, ты становишься Поваром и гордишься своей кухней.")
    israel_art_path = Path(__file__).resolve().parent.parent / "DATA" / "ARTS" / "ISRAEL_ART.txt"
    israel_art = load_art(israel_art_path)
    drawing_pics(israel_art)
    end()