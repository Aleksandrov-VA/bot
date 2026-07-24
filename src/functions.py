import re
import math
import random

def parse_user_query(message):
    pattern = r'([+-]?\d+(?:\.\d+)?)?\s*(плюс|минус|умножить\s+на|разделить\s+на|в\s+степени|корень\s+из)\s+([+-]?\d+(?:\.\d+)?)'
    regex_result = re.search(pattern, message.lower())

    if regex_result is not None:
        keys = ['number_1', 'operator', 'number_2']
        result = dict(zip(keys, regex_result.groups()))

        for key in ['number_1', 'number_2']:
            val = result[key]
            if val is not None and str(val).strip() != '':
                try:
                    result[key] = float(val)
                except ValueError:
                    return 'неверный формат ввода'
            else:
                result[key] = None

        return result
    return None

def chat_bot(message: str) -> str:
    response_dict = {
        'как дела': 'у меня всё хорошо, спасибо',
        'что ты умеешь': 'я умею отвечать на простые вопросы'
    }

    random_responses = ['интересный вопрос', 'я подумаю над этим', 'давайте сменим тему']
    unknown_answer = 'извините, я не знаю как ответить на это'

    math_operations = {
        'плюс':  lambda x, y: x + y,
        'минус': lambda x, y: x - y,
        'в степени':    lambda x, y: math.pow(x, y),
        'корень из':    lambda x, y: math.sqrt(y) if y > 0 else 'извлечение кв.корня из отрицательного числа',
        'умножить на':  lambda x, y: x * y,
        'разделить на': lambda x, y: x / y if y != 0 else 'деление на ноль',

    }

    if '/помощь' in message.lower():
        return ('\nдля выполнения математических операций, введите сообщение в следующем формате:\n'
                'сложение двух чисел A и B: сколько будет A плюс  B\n'
                'разность двух чисел A и B: сколько будет A минус B\n'
                'произведение двух чисел A и B: сколько будет A умножить на B\n'
                'результат деления A на B: сколько будет A разделить на B\n'
                'результат возведения числа A в степень B: сколько будет A в степени B\n'
                'значение квадратного корня из А: сколько будет корень из А\n')

    if 'сколько будет' in message.lower():
        query_components = parse_user_query(message)
        if query_components is not None:

            try:
                operator = query_components['operator']
                number_1 = query_components['number_1']
                number_2 = query_components['number_2']

                if operator in math_operations:
                    return f'результат {math_operations[operator](number_1, number_2)}'

            except (IndexError, ValueError, TypeError):
                return 'не могу обработать этот запрос, для более подробной информации введите "/помощь"'

    response = response_dict.get(message.lower(), unknown_answer)

    if response == unknown_answer:
        response = random.choice(random_responses)

    return response

# print(chat_bot("сколько будет корень из 9"))
# print(chat_bot("сколько будет корень из -0"))
# print(chat_bot("сколько будет -2.5 умножить на 9"))
# print(chat_bot("сколько будет 3.14 плюс 13"))
# print(chat_bot("сколько будет 2 минус  -1"))
# print(chat_bot("сколько будет 2 разделить на 2"))
print(chat_bot("сколько будет 2 в степени -2"))
print(chat_bot("помощь"))
