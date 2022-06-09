from datetime import timedelta
from nonebot import on_command, CommandSession, SenderRoles
from models.playerModel import *
from utils.jsonHelper import encode
from utils.sessionHelper import *
from utils.dbHelper import *
from utils.tools import *
import operator


# 打坐
@on_command('med', aliases=('打坐', '修炼'), only_to_me=False, permission=permission, run_timeout=timedelta(seconds=15))
async def info(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    # ctx = session.current_arg_text.strip()

    # 获取用户信息
    id = get_id(session)
    name = get_nickname(session)
    player = await PlayerModel.get_player(id)
    # 判断是否在修仙
    if not player.can_med():
        # 如果正在修仙，判断满300秒了嘛，没的话不让结束
        diff = get_current_timestamp() - player.last_med
        # 可以结束
        if diff >= 300:
            # 随机功力
            txt = ""
            # 10分钟内
            if diff <= 60 * 10:
                txt = "初窥门径"
                reward = get_rand_int(1,3)
            # 30分钟内
            elif diff <= 60 * 30:
                txt = "小有所成"
                reward = get_rand_int(2,5)
            # 60分钟内
            elif diff <= 60 * 60:
                txt = "受高人指点"
                reward = get_rand_int(3,8)
            # 60分钟以上
            else:
                txt = "感悟天地造化"
                reward = get_rand_int(5,10)
            # 更新数据
            player.energy += reward
            player.last_med = 0  # 取消打坐
            await player.save()
            # 配套的话
            ret = f"道友「{name}」已打坐{diff}秒，{txt}，获得{reward}功力（{player.energy}）"
            await session.send(ret)
        # 不能结束
        else:
            ret = f"道友「{name}」还在打坐中，请至少等待{300 - diff}秒"
            await session.send(ret)
    # 可以修仙就开始修仙
    else:
        player.last_med = get_current_timestamp()  # 开始打坐
        await player.save()
        # 向用户发送东西
        ret = f"道友「{name}」开始打坐"
        await session.send(ret)


# 功力榜
@on_command('energy_rank', aliases='功力榜', only_to_me=False, permission=permission, run_timeout=timedelta(seconds=15))
async def energy_rank(session: CommandSession):
    # 玩家自己的id
    id = get_id(session)
    name = get_nickname(session)
    group_id = get_group_id(session)
    # 玩家排名
    r = 0
    # 获取全部key
    keys = await get_keys(f"{get_player_key(None)}*")
    # 全部玩家
    ps = []
    # 获取玩家
    for k in keys:
        # key是player_id，需要用id获取对象
        player = await PlayerModel.get_player(str(k).split('_')[1])
        # 名字
        try:
            player.name = (await get_member(group_id, player.id)).nickname
        except:
            player.name = player.id
        # 记录
        ps.append(player)
    ps = sorted(ps, key=operator.attrgetter('energy'))[::-1]  # 降序
    for p in ps:
        # 玩家排名
        if p.id == id:
            r = ps.index(p) + 1
    ret = "【功力榜】\n"
    ret += '\n'.join([f"{ps.index(p)+1}. {p.name}：功力「{p.energy}」" for p in ps[:10]])
    ret += f"\n----------\n「{name}」排名：第{r}名"
    await session.send(ret)