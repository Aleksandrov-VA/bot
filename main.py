from src.conditions import respond_to_greeting
from src.functions  import chat_bot


print('Привет, добро пожаловать в чат-бот!')

while True:
    user_input = input('Пользователь: ')

    if  user_input.lower() == '/выход':
        print('Чат-бот: до свидания!')
        break

    greeting_response = respond_to_greeting(user_input)

    if greeting_response != 'Я тебя не понимаю!':
        response = greeting_response
    else:
        response = chat_bot(user_input)

    print(f'Чат-бот: {response}')