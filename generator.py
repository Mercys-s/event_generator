import random
import uuid
import os

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


def main():
    generator_user(os.getenv('COUNT_OF_USERS', \
                             int(input('Введите кол-во пользователей: '))))
    print(users_dict) #
    print('-------------------')
    
    for user_id, user_info in users_dict.items():
        user_action(user_id)
    
    print(event_dict)
    print('-------------------')




if __name__ == '__main__':
    
    main()
    

