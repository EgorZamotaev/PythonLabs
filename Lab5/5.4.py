from datetime import datetime, timedelta

date_birth = input("Введите дaту своего рождения в формате дд/мм/гггг ")
date_birth = date_birth.split("/")
date_birth = datetime(int(date_birth[2]), int(date_birth[1]), int(date_birth[0]))
now_date = datetime.now()
lived = now_date - date_birth
ave_death = 26333
death_date = date_birth + timedelta(days=ave_death)
rest_of_life = death_date - now_date

out = input("Введие желаемый формат вывода данных (minute, hour, day) ")
if out == 'minute':
    print("Прожито {} минут".format(int(lived.total_seconds()) // 60))
    print("Осталось прожить (предположительно) {} минут".format(int(rest_of_life.total_seconds()) // 60))
elif out == 'hour':
    print("Прожито {} часа".format(int(lived.total_seconds()) // 3600))
    print("Осталось прожить (предположительно) {} часов".format(int(rest_of_life.total_seconds()) // 3600))
elif out == 'day':
    print("Прожито {} дней".format(lived.days))
    print("Осталось прожить (передположительно) {} дней".format(rest_of_life.days))
else:
    print("Ошибка ввода")
