""" Создать  НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Что это значит? Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251,
а прочитать пытаетесь в utf-8.

Преподаватель будет запускать ваш скрипт и ошибок НЕ ДОЛЖНО появиться! """

from chardet import detect

with open(r'homework\task11\test_file.txt', 'rb') as f_n:
    cont_by = f_n.read()
detected = detect(cont_by)
print(detected)
encoding = detected['encoding']
content_text = cont_by.decode(encoding)

with open(r'homework\task11\test_file.txt', 'w', encoding = 'utf-8') as f_obj:
    f_obj.write(content_text)
print(content_text)


