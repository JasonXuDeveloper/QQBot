import time
import random
from nonebot import on_command, CommandSession, SenderRoles


JENGINE_GROUP_ID = 921271552
ET_GROUP_ID = 613752317
CUR_GROUP_ID = ET_GROUP_ID
ALLOW_LIST = [ET_GROUP_ID, 1076963479, 815388501]


# 随机数
def get_rand_int(min: int,max:int)->int:
    return random.randint(min,max)


# 现在时间
def get_current_timestamp() -> int:
    return int(time.time())


# 鉴权
def permission(sender: SenderRoles) -> bool:
    return sender.from_group(ALLOW_LIST)


# 鉴权
def is_je_group(sender: SenderRoles) -> bool:
    return sender.from_group(JENGINE_GROUP_ID)

