from utils.dbHelper import get_data_as_model_object, set_data_as_json
import asyncio


def get_player_key(id) -> str:
    if id is None:
        return "player_"
    return f"player_{id}"


class PlayerModel:
    def __init__(self, id: int):
        self._id = id  # QQ号
        self._atk = 1  # 攻击力
        self._hp = 1  # 血量
        self._def = 0  # 防御力
        self._doge = 0  # 闪避
        self._hit = 0  # 命中
        self._crit = 0  # 暴击
        self._res = 0  # 韧性
        self._critDmg = 150  # 暴击伤害百分比
        self._energy = 0  # 功力
        self._level = 0  # 境界
        self._last_med = 0  # 上次打坐时间

    def can_med(self) -> bool:
        """
        是否可打坐
        :return:
        """
        return self.last_med == 0

    def points(self) -> int:
        """
        可以加点
        :return:
        """
        return self.energy * 10 + 1 + 1 + 150 - self.atk - self.defence - self.hp -\
               self.doge - self.hit - self.crit - self.res - self.critDmg

    # 获取玩家数据
    @staticmethod
    async def get_player(id):
        key = get_player_key(id)
        player = await get_data_as_model_object(key)
        # 没有就注册并保存
        if not player:
            player = PlayerModel(id)
            # 保存
            await player.save()
        return player

    # 保存玩家数据
    async def save(self):
        key = get_player_key(self.id)
        await set_data_as_json(key, self)

    async def save_sync(self):
        asyncio.create_task(self.save())

    def get_level_name(self) -> str:
        """
        获取境界名
        :return:
        """
        ls = "筑基、开光、融合、心动、金丹、元婴、出窍、分神、合体、洞虚、大乘、渡劫".split('、')
        return ls[self.level]

    # 获取属性
    def get_member(self, member: str, def_val=None):
        if hasattr(self, member):
            return self.__dict__[member]
        else:
            # 尝试创建
            temp = PlayerModel(self.id)
            if hasattr(temp, member):
                temp.save_sync()
                setattr(self, member, temp.__dict__[member])
                return self.__dict__[member]
            else:  # 创建的也没就是真的没了
                return def_val

    @property
    def id(self):
        return self.get_member("_id", 0)

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def last_med(self):
        return self.get_member("_last_med", 0)

    @last_med.setter
    def last_med(self, value):
        self._last_med = value

    @property
    def energy(self):
        return self.get_member("_energy", 0)

    @energy.setter
    def energy(self, value):
        self._energy = value

    @property
    def level(self):
        return self.get_member("_level", 0)

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, value):
        self._atk = value

    @property
    def defence(self):
        return self._def

    @defence.setter
    def defence(self, value):
        self._def = value

    @property
    def doge(self):
        return self._doge

    @doge.setter
    def doge(self, value):
        self._doge = value

    @property
    def hit(self):
        return self._hit

    @hit.setter
    def hit(self, value):
        self._hit = value

    @property
    def crit(self):
        return self._crit

    @crit.setter
    def crit(self, value):
        self._crit = value

    @property
    def res(self):
        return self._res

    @res.setter
    def res(self, value):
        self._res = value

    @property
    def critDmg(self):
        return self._critDmg

    @critDmg.setter
    def critDmg(self, value):
        self._critDmg = value - 150
