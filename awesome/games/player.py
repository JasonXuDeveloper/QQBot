from datetime import timedelta
from nonebot import on_command, CommandSession, SenderRoles
from models.playerModel import *
from utils.jsonHelper import encode
from utils.sessionHelper import *
from utils.dbHelper import *
from utils.tools import *


# on_command 装饰器将函数声明为一个命令处理器
# 命令名字，别名，是否需要艾特了才能触发，然后鉴权
@on_command('info', aliases=('bt自视', 'bt属性'), only_to_me=False, permission=permission, run_timeout=timedelta(seconds=15))
async def info(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    # ctx = session.current_arg_text.strip()

    # 获取用户信息
    id = get_id(session)
    name = get_nickname(session)
    player = await PlayerModel.get_player(id)
    # 向用户发送东西
    ret = f"道友：{name}\n" \
          f"功力：{player.energy}\n" \
          f"境界：{player.get_level_name()}"
    await session.send(ret)
    # 等待输入内容
    more = (await session.aget(prompt='输入「更多」以查看其他数据，输入其他东西则会取消该会话')).strip()
    if more == "更多":
        ret = f"道友：{name}\n" \
              f"生命：{player.hp}\n" \
              f"攻击：{player.atk}\n" \
              f"防御：{player.defence}\n" \
              f"闪避：{player.doge}\n" \
              f"暴击：{player.crit}\n" \
              f"韧性：{player.res}\n" \
              f"暴击伤害：{player.critDmg}"
        await session.send(ret)


@on_command('add', aliases='bt加点', only_to_me=False, permission=permission, run_timeout=timedelta(seconds=30))
async def add_point(session: CommandSession):
    # 获取用户信息
    id = get_id(session)
    name = get_nickname(session)
    player = await PlayerModel.get_player(id)

    # 取得消息的内容，并且去掉首尾的空白符
    attrs = '\n'.join(f"- {x}" for x in ["生命", "攻击", "防御", "命中", "闪避", "暴击", "韧性", "暴击伤害"])
    ctx = (await session.aget(prompt=f'输入「属性=值」以加点（当前可用：{player.points()}），可以用空格分割以输入多个，例：「生命=3 攻击=1」，输入其他东西则会取消该会话\n'
                                     f'可以加点的属性列表：\n'
                                     f"{attrs}")).strip()
    # 分割需要加的属性
    ctx = ctx.replace('-','')  # 删除负数
    ctx = ctx.split(' ')
    # 全部点
    total_points = 0
    for c in ctx:
        val = int(c.split('=')[1])
        total_points += val
    if player.points() - total_points >= 0:  # 可用点数足够的情况下
        # 加点
        for c in ctx:
            n = c.split('=')[0]
            val = int(c.split('=')[1])
            if n == "生命":
                player.hp += val
            elif n == "攻击":
                player.atk += val
            elif n == "防御":
                player.defence += val
            elif n == "命中":
                player.hit += val
            elif n == "闪避":
                player.doge += val
            elif n == "暴击":
                player.crit += val
            elif n == "韧性":
                player.res += val
            elif n == "暴击伤害":
                player.critDmg += val
        # 保存
        await player.save()
        # 向用户发送东西
        ret = f"加点成功，\n" \
              f"道友：{name}\n" \
              f"生命：{player.hp}\n" \
              f"攻击：{player.atk}\n" \
              f"防御：{player.defence}\n" \
              f"命中：{player.hit}\n" \
              f"闪避：{player.doge}\n" \
              f"暴击：{player.crit}\n" \
              f"韧性：{player.res}\n" \
              f"暴击伤害：{player.critDmg}"
        await session.send(ret)
    else:
        await session.send("点数不足")