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