class PlayerModel:
    id = -1  # QQ号
    _atk = 1  # 攻击力
    _hp = 1  # 血量
    _def = 0  # 防御力
    _doge = 0  # 闪避
    _hit = 0  # 命中
    _crit = 0  # 暴击
    _res = 0  # 韧性
    _critDmg = 150  # 暴击伤害百分比

    def __init__(self, id: int):
        self.id = id
