# В этом файле находятся вспомогательные функции, которые генерируют информацию
# для метрик и параметров

import random

# Генеририрует параметры
def random_params(event_type, settings):
    params_dict = {}
    
    settings_list = settings[event_type]['params']
    if settings_list != None:
        for param in settings_list:
            params_dict[param] = generate_value(param)

        return params_dict
    
    else:
        return None

# Генеририрует метрики
def random_metrics(event_type, settings, is_success):
    metrics_dict = {}

    settings_list = settings[event_type]['metrics']
    for metric in settings_list:
        metrics_dict[metric] = generate_value(metric)

        # Нужно для выполнения условия, если произошла покупка/была отменена - звонок был успешен
        # Если событий всего 2 (Заход на сайт и звонок, то звонок был не успешный)
        if event_type == 2:
            metrics_dict['Успешно'] = is_success

    return metrics_dict


# Функция генерирующая непосредственно значения
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
    

