from nonebot.default_config import *
from datetime import timedelta

SESSION_EXPIRE_TIMEOUT = timedelta(minutes=2)  # 设置过期超时为 2 分钟，即用户 2 分钟不发消息后，会话将被关闭。
SUPERUSERS = {2313551611}  # 管理员
COMMAND_START = {'', '/', '!', '／', '！'}  # 解析任何命令，不需要特殊开头
