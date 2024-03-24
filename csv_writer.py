'''
Скрипт для записи событий в CSV

Принимает аргументом события (словарь event_data)

'''

import csv

def write_csv(event_data):
    
    with open('journal.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ('Идентификатор События', 'Тип События', 'Идентификатор Пользователя', 'Дата/Время', 'Источник ', \
             'Тип Устройства', 'Успешный ли звонок', 'Кол-во Просмотренных Страниц', 'Сумма заказа')
        )

        for event_id, event_info in event_data.items():
            
            writer.writerow(
                [
                event_info['id'],
                event_info['event_type'],
                event_info['user'],
                event_info['date_time'],

                event_info.get('parameters', {}).get('Источник', '') \
                if event_info.get('parameters') else '', 

                event_info.get('parameters', {}).get('Тип устройства', '') \
                if event_info.get('parameters') else '',  

                event_info.get('metrics', {}).get('Успешно', '') \
                if event_info.get('metrics') else '',  

                event_info.get('metrics', {}).get('Количество страниц', '') \
                if event_info.get('metrics') else '',  

                event_info.get('metrics', {}).get('Сумма заказа', '') \
                if event_info.get('metrics') else ''
                ]
            )