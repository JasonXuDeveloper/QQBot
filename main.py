import nonebot
import config
from os import path

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'game'),
        'awesome.game'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'basic'),
        'awesome.basic'
    )
    nonebot.run(host='127.0.0.1', port=8080)