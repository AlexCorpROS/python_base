from sys import argv
import time

script_name, work_hours, hourly_pay, reward = argv

print('Имя скрипта: ', script_name)
print('Отработано часов: ', work_hours)
print('Зарплата в час: ', hourly_pay)
print('Премия: ', reward)
print('Зарплата сотрудника: ', (float(work_hours) * float(hourly_pay)) + float(reward))

time.sleep(3) # для замедления отображения работы скрипта