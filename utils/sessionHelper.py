# <Event, {'post_type': 'message', 'message_type': 'group', 'time': 1654689930, 'self_id': 3114721675, 'sub_type':
# 'normal', 'user_id': 2313551611, 'message_id': -609000708, 'anonymous': None, 'font': 0, 'group_id': 921271552,
# 'raw_message': 'info', 'sender': {'age': 0, 'area': '', 'card': '', 'level': '', 'nickname': '傑', 'role': 'owner',
# 'sex': 'unknown', 'title': '', 'user_id': 2313551611}, 'message': [{'type': 'text', 'data': {'text': 'info'}}],
# 'message_seq': 270364, 'to_me': False}>
from nonebot import CommandSession


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
