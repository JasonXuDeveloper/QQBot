from nonebot import on_command, CommandSession, SenderRoles
from models.playerModel import *
from utils.jsonHelper import MyEncoder
from utils.sessionHelper import *
from utils.dbHelper import *


# 鉴权
def permission(sender: SenderRoles) -> bool:
    # 必须来自JE群
    return sender.from_group(921271552)


# 获取玩家key
def get_key(id : int) -> str:
    return f"player_{id}"


# on_command 装饰器将函数声明为一个命令处理器
# 命令名字，别名，是否需要艾特了才能触发，然后必须来自群（JEngine群921271552）才能处理
@on_command('info', aliases=('自视', '属性'), only_to_me=False, permission=permission)
async def info(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    # ctx = session.current_arg_text.strip()
    # 等待输入内容
    # await session.aget(prompt='你想查询哪个城市的天气呢？')

    # 获取用户信息
    id = get_id(session)
    key = get_key(id)
    player = await get_data_as_model_object(key)
    # 没有就注册并保存
    if not player:
        player = PlayerModel(id)
        # 保存
        await set_data_as_json(key, player)
    # 向用户发送东西
    await session.send(json.dumps(player, cls=MyEncoder))
