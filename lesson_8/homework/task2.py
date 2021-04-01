"""
2. * (вместо 1) Написать регулярное выражение для парсинга файла
логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),

например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""

# 93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 93.180.71.3 - - [17/May/2015:08:05:23 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"
# 80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)"


import re


re_log = re.compile(r'^((\d+\.){3}\d+) - - \[([^]]+)\] "([^ ]+) ([^ ]+) [^"]*" (\d+) (\d+) .*$')

with open('../../lesson_6/homework/nginx_logs.txt', 'r', encoding='utf-8') as f:
    for n, line in enumerate(f):
        match = re_log.match(line)
        if match:
            remote_addr = match.group(1)
            request_datetime = match.group(3)
            request_type = match.group(4)
            requested_resource = match.group(5)
            response_code = int(match.group(6))
            response_size = int(match.group(7))

            result = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)

            print(result)
        if n > 10:
            break
