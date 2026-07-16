#chapter1

from CORE.IMPERIVM_DEFS import apply_and_show_effects, choose_event, title


def chapter_1(player, all_chaps_data):
    input("Нажми Enter, чтобы начать новую главу"
          "\n ")
    title("ГЛАВА I: МОБИЛИЗАЦИЯ")
    print("Для твоих невероятных целей тебе нужны:")
    print("Сильная армия")
    print("Стабильная экономика")
    print("Хорошая дипломатия")

    # ЭКОНОМИКА
    print("\nНачнём с экономики. Она влияет на силу армии и стабильности в стране.")
    print(f"Очки экономики: {player.economy}")
    ec_event = choose_event(all_chaps_data["economy_events"], "экономику")
    apply_and_show_effects(player, ec_event)
    print("Открыта новая статистика! (3)")
    print("АВТОРИТЕТ - показывает твой авторитет среди населения. Влияет на боевой дух, силу армии и стабильность.")
    print("ЧЕСТЬ - показывает насколько твои действия соответствуют твоей личной философии. Влияет на авторитет.")
    print("=" * 60)

    # АРМИЯ
    print("\nТеперь надо заняться армией. Армия высчитывается из боевого духа, снабжения, науки, авторитета, вооружения и количества солдат.")
    print(f"Сила армии: {player.army_power}")
    arm_event = choose_event(all_chaps_data["army_events"], "армию")
    apply_and_show_effects(player, arm_event)
    print("Открыта новая статистика! (1)")
    print("СНАБЖЕНИЕ - отображает уровень логистики и провизии твоих врагов. Влияет на армию.")

    # ДИПЛОМАТИЯ
    print("\nПоследний шаг - дипломатия. Она влияет на способность создавать союзы.")
    print(f"Очки дипломатии: {player.diplomacy}")
    diplo_event = choose_event(all_chaps_data["diplomacy_events"], "дипломатию")
    apply_and_show_effects(player, diplo_event)
    return player