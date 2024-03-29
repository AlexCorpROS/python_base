""" Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице. """

import subprocess
import chardet

for sites in ['yandex.ru','youtube.com']:
    args = ['ping', sites]
    sites_ping = subprocess.Popen(args, stdout = subprocess.PIPE)
    for line in sites_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

