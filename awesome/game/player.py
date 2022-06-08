from datetime import timedelta

from nonebot import on_command, CommandSession, SenderRoles
from models.playerModel import *
from utils.jsonHelper import encode
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
@on_command('info', aliases=('自视', '属性'), only_to_me=False, permission=permission, run_timeout=timedelta(seconds=2))
async def info(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    # ctx = session.current_arg_text.strip()

    # 获取用户信息
    id = get_id(session)
    name = get_nickname(session)
    key = get_key(id)
    player = await get_data_as_model_object(key)
    # 没有就注册并保存
    if not player:
        player = PlayerModel(id)
        # 保存
        await set_data_as_json(key, player)
    # 向用户发送东西
    ret = f"""
    用户：{name}
    功力：{player.energy}
    境界：{player.get_level_name()}
    """
    await session.send(ret)
    # 等待输入内容
    more = (await session.aget(prompt='输入「更多」以查看其他数据')).strip()
    if more is "更多":
        ret = f"""
        用户：{name}
        血量：{player.hp}
        攻击力：{player.atk}
        防御力：{player.defence}
        闪避率：{player.doge}
        暴击率：{player.crit}
        韧性值：{player.res}
        暴击伤害：{player.critDmg}
        """
        await session.send(ret)