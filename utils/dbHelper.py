import json
import aioredis

pool = aioredis.ConnectionPool.from_url("redis://localhost", max_connections=10)
redis = aioredis.Redis(connection_pool=pool)


async def set_data(key: str, val: str):
    await redis.set(key, val)


async def set_data_as_json(key: str, val: object, cls):
    await redis.set(key, json.dumps(val, cls=cls))


async def get_data(key: str) -> str:
    return await redis.get(key)


async def get_data_as_object(key: str) -> object:
    d = await get_data(key)
    if d:
        return json.loads(d)
    return None


async def get_data_as_model_object(key: str, cls) -> object:
    d = await get_data(key)
    if d:
        return json.loads(d, cls=cls)
    return None
