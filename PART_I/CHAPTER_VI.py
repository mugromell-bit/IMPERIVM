from CORE.IMPERIVM_DEFS import new_chap, title


def chapter_6(player):
    new_chap()
    title("ГЛАВА VI: NEVER")
    if player.robert_whitemann:
        print("Ситуация с Лимой потихоньку забывается, Дум I прекращает активную экспансию и продолжает отказываться от союзов.")
        print("Но однажды тебе приходит письмо от Тёмного Короля.")
        print("В нём ")