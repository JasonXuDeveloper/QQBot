import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', aliases=['使用帮助', '帮助', '使用方法', '功能', '功能列表'], only_to_me=False)
async def usage(session: CommandSession):
    # 发送功能列表
    await session.send('功能列表：\n'
                       '-【属性】、【自视】，查看自身属性\n'
                       '-【打坐】、【修炼】，开始或结束打坐，并获得功力\n'
                       '-【加点】，增加属性点\n'
                       '-【功力榜】，记载功力最高的10位道友')
    return
