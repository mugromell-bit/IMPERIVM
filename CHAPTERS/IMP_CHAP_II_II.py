from CORE.IMPERIVM_DEFS import title, choose_event, apply_and_show_effects, war

morra_altair = {
    1: {
        "name": "Помочь Морре",
        "desc": "Ты отправляешь необходимую Морре помощь",
        "effects": {
            "diplomacy": 20,
            "army_size": -10_000_000,
            "supply": -10,
        }
    },
    2: {
        "name": "Сохранить нейтралитет",
        "desc": "Ты решаешь воздержаться от каких-либо действий.",
        "effects": {
            "diplomacy": -5,
        }
    },
    3: {
        "name": "Помочь Аль-Таире",
        "desc": "Ты делаешь неочевидный ход и помогаешь террористам.",
        "effects": {
            "diplomacy": -15,
        }
    }
}
def chapter_2_2(player):
    title("ГЛАВА II, Часть II: Скрытая Угроза")
    print(f"Авторитет: {player.authority}")
    print(f"Экономика: {player.economy}")
    print(f"Честь: {player.honor}")
    print(f"Вооружение: {player.armament}")
    print(f"Снабжение: {player.supply}")
    print(f"Дипломатия: {player.diplomacy}")
    print(f"Количество солдат: {player.army_size}")
    print(f"Мощь армии: {player.army_power}")
    print(f"Страх: {player.fear}")
    print("\n")
    print("Мирное время нарушает погром в Морре: террористическая группировка теократов «Аль-Таир». Они открыто заявляют о намерении захватить власть.")
    print("В связи с этим Литас просит тебя о помощи. Для борьбы он запрашивает:")
    print("10.000.000 солдат")
    print("10 очков снабжения.")
    print("Ты можешь:")
    mor_alt = choose_event(morra_altair, "войну Морры и Аль-Таиры")
    war()
    print("В ходе жестоких сражений Морра побеждает. Литас не забыл твоих действий.")
    apply_and_show_effects(player, mor_alt)
    return player


