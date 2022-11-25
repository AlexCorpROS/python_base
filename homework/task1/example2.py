"""  Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк. """

user_value = int(input('Введите количество секунд: '))

hours = user_value // 3600
minuts = (user_value - hours * 3600) // 60
seconds = (user_value - hours * 3600 - minuts * 60)
print(f'{user_value} секунд в формате чч:мм:сс имеет вид {hours}ч: {minuts}мин: {seconds}сек')
