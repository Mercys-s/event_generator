# В этом файле находятся вспомогательные функции, которые генерируют информацию
# для метрик и параметров

import random


def random_params(settings):
    params = {}
    



def random_metrics():
    pass


def generate_value(value_name):
    if value_name == 'Источник':
        return random.choice(['Яндекс', 'Гугл', 'Опера', 'Фейсбук', 'Инстаграмм'])
    
    elif value_name == 'Тип устройства':
        return random.choice(['Телефон', 'Планшет', 'Десктоп'])
    
    elif value_name == 'Сумма заказа':
        return random.randint(10000, 10000000)
    
    elif value_name == 'Количество страниц':
        return random.randint(1, 100)
    
    elif value_name == 'Успешно':
        return random.choice([True, False])
    

