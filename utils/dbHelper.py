import json
import aioredis
from utils.jsonHelper import *

pool = aioredis.ConnectionPool.from_url("redis://localhost", max_connections=10)
redis = aioredis.Redis(connection_pool=pool)


async def set_data(key: str, val: str):
    await redis.set(key, val)


async def set_data_as_json(key: str, val: object):
    await redis.set(key, encode(val))


async def get_data(key: str) -> str:
    return await redis.get(key)


async def get_data_as_model_object(key: str) -> object:
    d = await get_data(key)
    if d:
        return decode(d)
    return None
