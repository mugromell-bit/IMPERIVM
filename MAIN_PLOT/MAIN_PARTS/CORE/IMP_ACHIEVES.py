achievements = {
    "honor_40": {
        "name": "Родина",
        "condition": lambda p: p.honor >= 40,
        "desc": "За достижение 40 очков чести ты получаешь достижение!",
        "effects": {"authority": 5},
        "message": "Получено достижение 'Родина'! +5 авторитет"
    },

    "honor_100": {
        "name": "Слава нации!",
        "condition": lambda p: p.honor >= 100,
        "desc": "За достижение 100 очков чести ты получаешь достижение!",
        "effects": {"authority": 10, "propaganda": 5},
        "message": "Получено достижение 'Слава нации!'! +10 авторитет, +5 пропаганда"
    },

    "authority_40": {
        "name": "Даже не ручка",
        "condition": lambda p: p.authority >= 40,
        "desc": "За достижение 40 очков авторитета ты получаешь достижение!",
        "effects": {"economy": 5, "propaganda": 5, "diplomacy": 10},
        "message": "Получено достижение 'Даже не ручка'! +5 экономика, +5 пропаганда, +10 дипломатия"
    },

    "authority_100": {
        "name": "Бесконечный респект",
        "condition": lambda p: p.authority >= 100,
        "desc": "За достижение 100 очков авторитета ты получаешь достижение!",
        "effects": {"economy": 15, "propaganda": 5, "honor": 10},
        "message": "Получено достижение 'Бесконечный респект'! +15 экономика, +5 пропаганда, +10 честь"
    },

    "economy_40": {
        "name": "Финансовая грамотность",
        "condition": lambda p: p.economy >= 40,
        "desc": "За достижение 40 очков экономики ты получаешь достижение!",
        "effects": {"supply": 5, "authority": 5},
        "message": "Получено достижение 'Финансовая грамотность'! +5 снабжение, +5 авторитет"
    },

    "economy_100": {
        "name": "Блэкшильд",
        "condition": lambda p: p.economy >= 100,
        "desc": "За достижение 100 очков экономики ты получаешь достижение!",
        "effects": {"supply": 10, "authority": 10},
        "message": "Получено достижение 'Блэкшильд'! +10 снабжение, +10 авторитет"
    },

    "fight_spirit_40": {
        "name": "Зов предков",
        "condition": lambda p: p.fight_spirit >= 40,
        "desc": "За достижение 40 очков боевого духа ты получаешь достижение!",
        "effects": {"fear": 5},
        "message": "Получено достижение 'Зов предков'! +5 страх"
    },

    "fight_spirit_100": {
        "name": "Храброе сердце",
        "condition": lambda p: p.fight_spirit >= 100,
        "desc": "За достижение 100 очков боевого духа ты получаешь достижение!",
        "effects": {"fear": 10},
        "message": "Получено достижение 'Храброе сердце'! +10 страх"
    },

    "army_power_40": {
        "name": "Македонский",
        "condition": lambda p: p.army_power >= 40,
        "desc": "За достижение 40 очков военной мощи ты получаешь достижение!",
        "effects": {"fear": 5, "propaganda": 5},
        "message": "Получено достижение 'Македонский'! +5 страх, +5 пропаганда"
    },

    "army_power_100": {
        "name": "Generale, Generale",
        "condition": lambda p: p.army_power >= 100,
        "desc": "За достижение 100 очков военной мощи ты получаешь достижение!",
        "effects": {"fear": 10, "propaganda": 5},
        "message": "Получено достижение 'Generale, Generale'! +10 страх, +5 пропаганда"
    },

    "stability_40": {
        "name": "Метроном",
        "condition": lambda p: p.stability >= 40,
        "desc": "За достижение 40 очков стабильности ты получаешь достижение!",
        "effects": {"diplomacy": 5, "propaganda": 5},
        "message": "Получено достижение 'Метроном'! +5 дипломатия, +5 пропаганда"
    },

    "stability_92": {
        "name": "На веки",
        "condition": lambda p: p.stability >= 92,
        "desc": "За достижение 92 очков стабильности ты получаешь достижение!",
        "effects": {"diplomacy": 20, "propaganda": 5},
        "message": "Получено достижение 'На веки'! +20 дипломатия, +5 пропаганда"
    },

    "diplomacy_40": {
        "name": "Есть контакт",
        "condition": lambda p: p.diplomacy >= 40,
        "desc": "За достижение 40 очков дипломатии ты получаешь достижение!",
        "effects": {"economy": 5, "supply": 5},
        "message": "Получено достижение 'Есть контакт'! +5 экономика, +5 наука"
    },

    "diplomacy_100": {
        "name": "Белый Крест",
        "condition": lambda p: p.diplomacy >= 100,
        "desc": "За достижение 100 очков дипломатии ты получаешь достижение!",
        "effects": {"economy": 10, "supply": 5},
        "message": "Получено достижение 'Белый Крест'! +10 экономика, +15 наука"
    },

    "propaganda_40": {
        "name": "Про Нас",
        "condition": lambda p: p.propaganda >= 40,
        "desc": "За достижение 40 очков пропаганды ты получаешь достижение!",
        "effects": {"honor": 5, "authority": 5},
        "message": "Получено достижение 'Про Нас'! +5 честь, +5 авторитет"
    },

    "propaganda_100": {
        "name": "Чистокровный",
        "condition": lambda p: p.propaganda >= 100,
        "desc": "За достижение 100 очков пропаганды ты получаешь достижение!",
        "effects": {"honor": 10, "authority": 10},
        "message": "Получено достижение 'Чистокровный'! +10 честь, +10 авторитет"
    },

    "espionage_40": {
        "name": "Сталкер",
        "condition": lambda p: p.espionage >= 40,
        "desc": "За достижение 40 очков шпионажа ты получаешь достижение!",
        "effects": {"fear": 5, "armament": 5},
        "message": "Получено достижение 'Сталкер'! +5 страх, +5 наука"
    },

    "espionage_100": {
        "name": "007",
        "condition": lambda p: p.espionage >= 100,
        "desc": "За достижение 100 очков шпионажа ты получаешь достижение!",
        "effects": {"fear": 10, "armament": 10},
        "message": "Получено достижение '007'! +10 страх, +10 наука"
    },

    "fear_40": {
        "name": "Мурзик",
        "condition": lambda p: p.fear >= 40,
        "desc": "За достижение 40 очков страха ты получаешь достижение!",
        "effects": {"diplomacy": 5},
        "message": "Получено достижение 'Мурзик'! +5 дипломатия"
    },

    "fear_100": {
        "name": "УSатые ВойSка",
        "condition": lambda p: p.fear >= 100,
        "desc": "За достижение 100 очков страха ты получаешь достижение!",
        "effects": {"diplomacy": 5},
        "message": "Получено достижение 'УSатые ВойSка'! +5 дипломатия"
    },

    "supply_40": {
        "name": "Налегке",
        "condition": lambda p: p.supply >= 40,
        "desc": "За достижение 40 очков снабжения ты получаешь достижение!",
        "effects": {"propaganda": 5},
        "message": "Получено достижение 'Налегке'! +5 пропаганда"
    },

    "supply_100": {
        "name": "Рука помощи",
        "condition": lambda p: p.supply >= 100,
        "desc": "За достижение 100 очков снабжения ты получаешь достижение!",
        "effects": {"propaganda": 5},
        "message": "Получено достижение 'Рука помощи'! +5 пропаганда"
    },

    "armament_40": {
        "name": "Bosanska artiljerija",
        "condition": lambda p: p.armament >= 40,
        "desc": "За достижение 40 очков вооружения ты получаешь достижение!",
        "effects": {"supply": 5, "propaganda": 5},
        "message": "Получено достижение 'Зубастый'! +5 снабжение, +5 пропаганда"
    },

    "armament_100": {
        "name": "Палки и камни",
        "condition": lambda p: p.armament >= 100,
        "desc": "За достижение 100 очков вооружения ты получаешь достижение!",
        "effects": {"supply": 10, "propaganda": 5},
        "message": "Получено достижение 'Палки и камни'! +10 снабжение, +5 пропаганда"
    }
}


def check_achievements(player):
    new_unlocked = []
    for ach_id, ach in achievements.items():
        if ach_id in player.unlocked_achievements:
            continue
        if ach["condition"](player):
            for stat, value in ach["effects"].items():
                if hasattr(player, stat):
                    old = getattr(player, stat)
                    setattr(player, stat, old + value)
            print(ach["desc"])
            print(ach["message"])
            new_unlocked.append(ach_id)
    return new_unlocked
