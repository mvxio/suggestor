import json
import ssl
from urllib.parse import quote
from urllib.request import urlopen

RAINBOW_CATALOG = [
    "Администратор", "Подработка", "Водитель", "Менеджер",
    "Продавец", "Помощник руководителя", "Помощник",
    "Специалист", "Курьер", "Секретарь", "Кладовщик",
    "Оператор", "Бухгалтер", "Юрист", "Охранник",
    "Руководитель", "Экономист", "Официант", "Мерчендайзер",
    "Директор", "Уборщица", "Инженер", "Супервайзер",
    "Кассир", "Грузчик", "Повар", "Дизайнер",
    "Сварщик", "Системный администратор", "Программист", "Электрик"
]

def get_suggests(text):
    url =f'https://api.hh.ru/suggests/positions?text={quote(text)}' 
    resp = urlopen(url, context=ssl._create_unverified_context())
    return json.loads(resp.read().decode('utf-8'))


def describe_suggests(text, suggests):
    items = suggests.get("items")
    if not items:
        return f'There is no suggests for {text}'
    
    n_suggests = len(items)
    specs = items[0].get('specializations')[0]
    return f'Suggests for {text} len: {n_suggests} ' \
        + f'specialization_id: {specs.get("id")} ' \
        + f'profarea_id: {specs.get("profarea_id")} ' 


def print_rainbow_catalog_info():
    for item in RAINBOW_CATALOG:
        suggests = get_suggests(item)
        print(describe_suggests(item, suggests))


if __name__ == '__main__':
    print_rainbow_catalog_info()
