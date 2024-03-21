def generator_user():
    pass

def generator_event(id, event_type , user_id , date_time, **kwargs):
    pass

# предположительно это **kwargs
kwargs = {
    'params': {
        'Источник': 'переменная',
        'Тип устройства': 'переменная',
    },
    'metrics': {
        'Сумма заказа': 'переменная (int)',
        'Количество страниц': 'переменная (int)',
        'Успешно': 'переменная (bool)'
    }
}

success_metric = ['Успешно']
settings = {
    1: {
        'params': ['Источник', 'Тип браузера',],
        'metrics': ['Количество страниц',]
    },

    2: {
        'params': ['Источник',],
        'metrics': success_metric
    },

    3: {
        'params': None,
        'metrics': ['Сумма заказа'] + success_metric
    },

    4: {
        'params': None,
        'metrics': ['Сумма заказа'] + success_metric
    }
}
