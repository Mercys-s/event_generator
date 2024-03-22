import random
import uuid
import os


from datetime import datetime
from faker import Faker

# Определяется язык, для библеотеки, придумывающей информацию
fake = Faker('ru_RU')



users = {}
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

        users[user_id] = user_information

    return f'Список из "{count_of_users}" пользователя(ей) был создан'
    

event_dict = {}
def generator_event(event_type , user_id , date_time, **kwargs):
    event_id = str(uuid.uuid4())

    event_information = {
        'id': event_id,
        "event_type": event_type,
        'user': user_id,
        'date_time': date_time,
        **kwargs
    }

    event_dict[event_id] = event_information

    return 'Событие сгенерировано'


def user_action(user_id, **kwargs):
    events = random.randint(1,4)

    for not_correct_event_type in range(events):
        event_type = not_correct_event_type + 1
        date_time = datetime.now()

        generator_event(event_type = event_type, user_id = user_id, date_time = date_time, **kwargs)


def main():
    generator_user(os.getenv('COUNT_OF_USERS', \
                             input('Введите кол-во пользователей')))
    for user in users:

        user_action(user['id'], )

# предположительно это **kwargs
some_kwargs = {
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


