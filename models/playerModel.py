class PlayerModel:
    def __init__(self, id: int):
        self.id = id # QQ号
        self._atk = 1  # 攻击力
        self._hp = 1  # 血量
        self._def = 0  # 防御力
        self._doge = 0  # 闪避
        self._hit = 0  # 命中
        self._crit = 0  # 暴击
        self._res = 0  # 韧性
        self._critDmg = 150  # 暴击伤害百分比
        self.energy = 0  # 功力
        self.level = 1  # 境界

    def get_level_name(self) -> str:
        """
        获取境界名
        :return:
        """
        ls = "筑基、开光、融合、心动、金丹、元婴、出窍、分神、合体、洞虚、大乘、渡劫".split('、')
        return ls[self.level]

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def defence(self):
        return self._def

    @property
    def doge(self):
        return self._doge

    @property
    def crit(self):
        return self._crit

    @property
    def res(self):
        return self._res

    @property
    def critDmg(self):
        return self._critDmg