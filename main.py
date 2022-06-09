import nonebot
import config
from os import path


if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'games'),
        'awesome.games'
    )
    nonebot.run(host='127.0.0.1', port=8080)