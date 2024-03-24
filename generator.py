'''
Файл содержит в себе:  
1. Генератор пользователей,
2. Генератор событий,
3. Иммитацию действия пользователя

Случайные данные реализуются с помощью: 
1. Библиотеки faker (имена пользователей)
2. Библиотеки uuid (ID-шники пользователей, событий)
3. Библиотеки datetime
'''

import random
import uuid

from settings import settings
from params_metrics import random_metrics, random_params
from csv_writer import write_csv

from datetime import datetime
from faker import Faker

fake = Faker('ru_RU')


users_data = {}
def generator_user(count_of_users):
    '''
    Генерирует пользователей и собирает их в словарь
    users_data

    Аргументом принимает кол-во генерируемых юзеров

    '''
    for _ in range(1, count_of_users + 1):

        user_id = str(uuid.uuid4())
        user_name = fake.name()
        user_age = random.randint(18,70)

        user_information = {
            'id': user_id,
            'name': user_name,
            'age': user_age,
        }

        users_data[user_id] = user_information

    return f'Список из "{count_of_users}" пользователя(ей) был создан'
    

event_data = {}
def generator_event(event_type , user_id , date_time, is_success):
    '''
    Генерирует события и собирает их в словарь
    event_data для последущей записи в csv-файл

    Аргументом принимает:
    1. Тип события (int)   3. Дату события (str)
    2. ID юзеров (str)     4. Был ли успешен звонок (bool)

    Внутри генератора событий используются функции для
    создания параметров и метрик
    '''
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

    event_data[event_id] = event_information

    return f'Событие {event_id} сгенерировано'


def user_action(user_id):
    '''
    В этой функции имитируется действие пользователя:
    1. Определяется сколько событий будет у юзера (1-4)
    2. Определяется успешность звонка
    3. Создается дата/время события

    Аргументом принимает:
    1. ID юзеров (str), которые приходят из users_data

    '''
    events = random.randint(1,4)
    is_success = True if events > 2 else False

    for not_correct_event_type in range(events):
        event_type = not_correct_event_type + 1

        date_time_unformated = datetime.now()
        date_time = date_time_unformated.strftime('%Y-%m-%d %H:%M:%S')

        generator_event(event_type = event_type, user_id = user_id,\
                        date_time = date_time, is_success = is_success)


def main():
    '''
    Главная функция:
    1. Проверяет корректность входных данных
    2. Запускает генератор пользователей
    3. Определяет, какой пользователь, какие события вызвал
    4. Созданные события запсываются в итоговый CSV-файл

    '''
    try:
        count_of_users = int(input('Введите кол-во пользователей: '))
    except:
        raise ValueError('Используйте числовое значение')

    generator_user(count_of_users)

    for user_id, user_info in users_data.items():
        user_action(user_id)
    
    write_csv(event_data)


if __name__ == '__main__':
    main()
    

