def parse_config():
    try:
        import json
        from os import environ

        config = json.load(open('config.json', 'r', encoding='utf-8'))
        environ['bot_name'] = config['BOT']['NAME']
        environ['bot_token'] = config['BOT']['TOKEN']
        environ['bot_admins'] = json.dumps(config['BOT']['ADMINS'])

    except Exception:
        raise Exception('ERROR: Invalid config')


def start_bot():
    try:
        from bot import bot

        bot.polling(none_stop=True)

    except Exception:
        raise Exception('ERROR: Failed to start bot')


if __name__ == '__main__':
    parse_config()
    start_bot()