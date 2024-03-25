'''
Файл содержит тесты на:
1. Проверку, работает ли генератор событий в целом
2. Проверку на формирование данных генератора событий
'''

import sys
sys.path.append("./")

import pytest

from settings import settings
from generator import generator_event
from params_metrics import random_metrics, random_params


@pytest.mark.parametrize('event_type , user_id , date_time, is_success', [
                                (1, '34532', '2022-01-01 6:00:00', True),
                                (2, '34532', '2022-01-02 8:00:00', True),
                                (3, '34532', '2022-01-03 5:00:00', True),
                                (1, '534532', '2022-02-01 11:00:00', False),
                                (2, '534532', '2022-03-02 10:00:00', False),
                                                                         ])
def test_generator_event_success(event_type , user_id , date_time, is_success):
    '''
    Этот тест проверяет, успешно ли завершается функция
    генератора событий, при заданных параметрах
    '''
    result = generator_event(event_type , user_id , date_time, is_success)

    assert result.startswith('Событие')



@pytest.mark.parametrize('event_id, event_type , user_id , date_time, is_success', [
                        ('2343-ert322', 1, '34532', '2022-01-01 6:00:00', True),
                                                                         ])
def test_generator_event_data(event_id, event_type , user_id , date_time, is_success):
    '''
    Тест принимает входные данные, как у функции generator_event
    и идет проверка формирования данных события 
    '''
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

    assert event_information['id'] == event_id
    assert event_information['event_type'] == event_type
    assert event_information['user'] == user_id
    assert event_information['date_time'] == date_time
    assert event_information['parameters'] == parameters
    assert event_information['metrics'] == metrics


