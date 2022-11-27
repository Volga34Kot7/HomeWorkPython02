# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

money = int(input('Введите сумму заработной платы: '))
count_25, count_10, count_5, count_1 = 0, 0, 0, 0
while money != 0:
    if money > 25:
        count_25 += 1
        money = money - 25
    elif money > 10:
        count_10 += 1
        money = money - 10
    elif money > 5:
        count_5 += 1
        money = money - 5
    elif money > 1:
        count_1 += 1
        money = money - 1
        break

print(f'Купюры: \n25 руб. - {count_25},'
      f'\n10 руб. - {count_10},'
      f'\n5 руб. - {count_5},'
      f'\n1 руб. - {count_1}')