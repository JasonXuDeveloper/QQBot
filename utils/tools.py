import time
import random
from nonebot import on_command, CommandSession, SenderRoles
import functools


JENGINE_GROUP_ID = 921271552
ET_GROUP_ID = 688386209
CUR_GROUP_ID = JENGINE_GROUP_ID
ALLOW_LIST = [JENGINE_GROUP_ID, ET_GROUP_ID, 1076963479, 815388501]


# 随机数
def get_rand_int(min: int,max:int)->int:
    return random.randint(min,max)


# 现在时间
def get_current_timestamp() -> int:
    return int(time.time())


# 鉴权
def permission(sender: SenderRoles) -> bool:
    # 必须来自JE群
    return sender.from_group(ALLOW_LIST)
