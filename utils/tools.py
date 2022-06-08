import time
import random
from nonebot import on_command, CommandSession, SenderRoles


# 随机数
def get_rand_int(min: int,max:int)->int:
    return random.randint(min,max)


# 现在时间
def get_current_timestamp() -> int:
    time.time()


# 鉴权
def permission(sender: SenderRoles) -> bool:
    # 必须来自JE群
    return sender.from_group(921271552)