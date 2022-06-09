import imp
import nonebot
import config
from os import path
from utils.sessionHelper import *
from utils.dbHelper import *
from models.playerModel import *


async def f():
    # 玩家排名
    r = 0
    # 获取全部key
    keys = await get_keys(f"{get_player_key(None)}*")
    print(keys)
    # 全部玩家
    ps = []
    # 获取玩家
    for k in keys:
        # key是player_id，需要用id获取对象
        player = await PlayerModel.get_player(k.split('_')[1])
        # 名字
        player.name = await get_member(921271552, player.id)
        # 记录
        ps.append(player)
    print(ps)

if __name__ == '__main__':
    asyncio.create_task(f()) 
    # nonebot.init(config)
    # nonebot.load_plugins(
    #     path.join(path.dirname(__file__), 'awesome', 'plugins'),
    #     'awesome.plugins'
    # )
    # nonebot.load_plugins(
    #     path.join(path.dirname(__file__), 'awesome', 'games'),
    #     'awesome.games'
    # )
    # nonebot.run(host='127.0.0.1', port=8080)