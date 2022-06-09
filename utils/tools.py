import time
import random
from nonebot import on_command, CommandSession, SenderRoles
import functools


# 随机数
def get_rand_int(min: int,max:int)->int:
    return random.randint(min,max)


# 现在时间
def get_current_timestamp() -> int:
    return int(time.time())


# 鉴权
def permission(sender: SenderRoles) -> bool:
    # 必须来自JE群
    return sender.from_group(921271552)


def force_sync(fn):
    '''
    turn an async function to sync function
    '''
    import asyncio

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        if asyncio.iscoroutine(res):
            asyncio.create_task(fn(*args, **kwargs)) 
        return res

    return wrapper