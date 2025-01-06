from datetime import date, datetime # включаем библиотеки datetime для работы с датами

today_date = date.today() # узнаем сегодняшнюю дату
print("Текущая дата: {}-{}-{}".format(today_date.day, today_date.month, today_date.year))
while True: # цикл для определения корректной даты ввода
    issue_date = input("Введите дату дедлайна (в формате 'день-месяц-год'): ")
    try:
        issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
        break
    except ValueError as e:
        print(e)
# определение количества дней между сегодняшней и введенной латами
date1 = datetime(today_date.year, today_date.month, today_date.day)
date2 = datetime(issue_date.year, issue_date.month, issue_date.day)
delta = (date2 - date1).days
# определение корректного окончания слова в зависимости от количества дней
day = 'дней'
if abs(delta) % 10 == 1:
    day = 'день'
elif 1 < abs(delta) % 10 < 5:
    day = 'дня'
# вывод информации о дедлайне
if delta < 0:
    print(f"Внимание! Дедлайн истёк {abs(delta)} {day} назад") # Вывод предупреждения об истечении срока дедлайна
elif delta > 0:
    print(f"До дедлайна осталось {delta} {day}")  # Вывод предупреждения о дедлайне
else:
    print('Дедлайн сегодня!')
