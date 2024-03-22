import random
import uuid
import os
import csv

from settings import settings
from params_metrics import random_metrics, random_params

from datetime import datetime
from faker import Faker

# Определяется язык, для библеотеки, придумывающей информацию
fake = Faker('ru_RU')


users_dict = {}
def generator_user(count_of_users):
    for _ in range(1, count_of_users + 1):

        user_id = str(uuid.uuid4())
        user_name = fake.name()
        user_age = random.randint(18,70)

        user_information = {
            'id': user_id,
            'name': user_name,
            'age': user_age,
        }

        users_dict[user_id] = user_information

    return f'Список из "{count_of_users}" пользователя(ей) был создан'
    

event_dict = {}
def generator_event(event_type , user_id , date_time, is_success):
    event_id = str(uuid.uuid4())

    parameters = random_params(event_type, settings)
    metrics = random_metrics(event_type, settings, is_success)

    event_information = {
        'id': event_id,
        'event_type': event_type,
        'user': user_id,
        'date_time': date_time,
        'parameters': parameters,
        'metrics': metrics
    }

    event_dict[event_id] = event_information

    return f'Событие {event_id} сгенерировано'


def user_action(user_id):
    events = random.randint(1,4)
    is_success = True if events > 2 else False

    for not_correct_event_type in range(events):
        event_type = not_correct_event_type + 1

        date_time_unformated = datetime.now()
        date_time = date_time_unformated.strftime('%Y-%m-%d %H:%M:%S')

        generator_event(event_type = event_type, user_id = user_id,\
                        date_time = date_time, is_success = is_success)


# Запись в csv файл
def write_csv():
    
    with open('journal.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ('Идентификатор События', 'Тип События', 'Идентификатор Пользователя', 'Дата/Время', 'Источник ', \
             'Тип Устройства', 'Успешный ли звонок', 'Кол-во Просмотренных Страниц', 'Сумма заказа')
        )

        for event_id, event_info in event_dict.items():
            
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


def main():
    
    # Генерация пользователей
    generator_user(int(input('Введите кол-во пользователей: ')))

    # Сам процесс, имитация действий пользователей
    for user_id, user_info in users_dict.items():
        user_action(user_id)
    
    # Запись результатов в CSV файл
    write_csv()


if __name__ == '__main__':
    main()
    

