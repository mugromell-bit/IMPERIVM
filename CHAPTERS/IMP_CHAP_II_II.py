from CORE.IMPERIVM_DEFS import title, choose_event, apply_and_show_effects, war

def chapter_2_2(player, all_chaps_data):
    input("Нажми Enter, чтобы начать новую главу"
          "\n ")
    title("ГЛАВА II, Часть II: СКРЫТАЯ УГРОЗА")
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
    print("Мирное время нарушает погром в Морре: террористическая группировка теократов «Аль-Таир» открыто заявляет о намерении захватить власть.")
    print("В связи с этим Литас просит тебя о помощи. Для борьбы он запрашивает:")
    print("10.000.000 солдат")
    print("10 очков снабжения.")
    print("Ты можешь:")
    mor_alt = choose_event(all_chaps_data["morra_altair"], "войну Морры и Аль-Таиры")
    war()
    print("В ходе жестоких сражений Морра побеждает. Литас не забыл твоих действий.")
    apply_and_show_effects(player, mor_alt)
    return player


