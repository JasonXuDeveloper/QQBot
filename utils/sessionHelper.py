# <Event, {'post_type': 'message', 'message_type': 'group', 'time': 1654689930, 'self_id': 3114721675, 'sub_type':
# 'normal', 'user_id': 2313551611, 'message_id': -609000708, 'anonymous': None, 'font': 0, 'group_id': 921271552,
# 'raw_message': 'info', 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': '傑', 'role': 'owner',
# 'sex': 'unknown', 'title': '', 'user_id': 2313551611}, 'message': [{'type': 'text', 'data': {'text': 'info'}}],
# 'message_seq': 270364, 'to_me': False}>
from nonebot import CommandSession
import nonebot


def get_nickname(sender: CommandSession) -> str:
    """
    获取名字
    :param sender:
    :return:
    """
    return str(sender.event.sender['nickname'])


def get_id(sender: CommandSession) -> int:
    """
    获取id
    :param sender:
    :return:
    """
    return int(sender.event.user_id)


def get_group_id(sender: CommandSession) -> int:
    """
    获取groupid
    :param sender:
    :return:
    """
    return int(sender.event.group_id)


async def get_member(group_id: int, user_id: int):
    """
    {'age': 0, 'area': '', 'card': '', 'card_changeable': False, 'group_id': 815388501, 'join_time': 1654755232,
    'last_sent_time': 1654755387, 'level': '1', 'nickname': '傑', 'role': 'owner', 'sex': 'unknown',
    'shut_up_timestamp': 0, 'title': '', 'title_expire_time': 0, 'unfriendly': False, 'user_id': 2313551611}
    :param group_id:
    :param user_id:
    :return:
    """
    bot = nonebot.get_bot()
    ret = await bot.get_group_member_info(group_id=group_id, user_id=user_id)
    return ret
