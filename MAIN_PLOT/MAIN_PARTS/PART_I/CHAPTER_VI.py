from MAIN_PLOT.CORE.IMPERIVM_DEFS import new_chap, title

def accept_adam_cult(player):
    print("Ты принял предложение Адама. Ты скорейшим способом отрёкся от правления и, ожидая последующих инстукрций, пытаешься скрыться от разбушевавшихся радикалов.")
    print("Пути обратно нет. Твой авторитет пал, тебя называют предателем родины и объявляют в розыск.")
    player.adam_kreuz_accept = True
    return player
    # После этого со старым классом player взаимодействий не будет.

def read_kreuz_letter(player):
    print("Ты решил прочитать письмо Адама.")
    print("В своём коротком, но очень ярком послании Адам рассказывает о концепции Неизбежного.")
    print("Он пытается убедить тебя в том, что единственный способ исправить свою ошибку — это оставить правление и следовать за ним. Это твой единственный шанс.")
    print("Куда именно следовать и что будет в конце он не объясняет.")
    print("ADAM KREUZ. NOW OR NEVER.")
    if player.espionage >= 10:
        print("Твои разведчики докладывают, что похожие письма пришли Гордону Хартманну, Анту и Деметриусу.")
    print("\n")
    print("Принимаешь ли ты это предложение?")
    print("1 - Нет")
    print("2 - ¡YES!")
    while True:
        try:
            choice = int(input(">>> "))
            if choice == 1:
                print("Ты выкидываешь письмо и забываешь об этом безумце.")
                break
            elif choice == 2:
               accept_adam_cult(player)
            break
        except ValueError:
            print("Введи число!")


def chapter_6(player):
    new_chap()
    title("ГЛАВА VI: NEVER")
    print("Тебе приходит письмо от некого Адама Крёйца. Советники предупреждают, что это очередной космист-шизофреник и воспринимать всерьёз его не стоит.")
    print("Будешь читать?")
    print("1 - Нет")
    print("2 - Да")
    while True:
        try:
            choice = int(input(">>> "))
            if choice == 1:
                print("Ты выкидываешь письмо даже не распечатав.")
                break
            elif choice == 2:
                read_kreuz_letter(player)
                return player
        except ValueError:
            print("Введи число!")
    print("\nНаконец, после всех геополитических приколов, космошизоидов и интриг, ты можешь начать настоящую конкуренцию.")
    title("КОНЕЦ ПЕРВОЙ ЧАСТИ")
    return player

