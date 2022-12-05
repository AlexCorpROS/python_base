""" Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой. """

def user_data (name, surname, year_birth, city_residence, email, phone):     
    return print(f'Имя: {name} Фамилия: {surname} Год рождения: {year_birth} Город проживания: {city_residence}'
    f' Email: {email} Телефон: {phone}')

user_data(name = input('Введите Имя: '),
    surname = input('Введите Фамилию: '),
    year_birth = input('Введите год рождения: '),
    city_residence = input('Введите город проживания: '),
    email = input('Введите email: '),
    phone = input('Введите телефон: '),)
