from utils.tools import *


@on_command('usage', aliases=['bt帮助', 'bt使用方法', 'bt功能', 'bt功能列表'], permission=permission, only_to_me=False)
async def usage(session: CommandSession):
    # 发送功能列表
    await session.send('功能列表：\n'
                       '-【bt属性】、【bt自视】，查看自身属性\n'
                       '-【bt打坐】、【bt修炼】，开始或结束打坐，并获得功力\n'
                       '-【bt加点】，增加属性点\n'
                       '-【bt功力榜】，记载功力最高的10位道友')
    return


@on_command('bug', patterns=['.*报错', '.*错误', ".*bug"], permission=is_je_group, only_to_me=False)
async def err(session: CommandSession):
    # 发送功能列表
    await session.send('可以看看文档有没有提到：https://docs.xgamedev.net/zh/documents/0.7/')
    return
