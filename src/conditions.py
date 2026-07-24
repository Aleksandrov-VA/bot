def respond_to_greeting(message: str) -> str:
    greetings = ['привет', 'здравствуйте', 'добрый день']
    farewells = ['пока', 'до свидания', 'прощай']

    if message.lower() in greetings:
        return 'И тебе привет!'
    elif message.lower() in farewells:
        return 'давай до свидания!'
    else:
        return 'Я тебя не понимаю!'