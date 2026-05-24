from app.variables.banners import *

class BannerFactory:
    def create(entity, action, critical = False):
        match (entity, action, critical):
            case ("Hero", "attack", False):
                return heroAttack
            case ("Hero", "attack", True):
                return heroCritical
            case ("Hero", "defend", False):
                return heroDefending
            case ("Hero", "evade", False):
                return heroEvading
            case ("Monster", "attack", False):
                return monsterAttack
            case ("Monster", "attack", True):
                return monsterCritical
            case ("Monster", "defend", False):
                return monsterDefending
            case ("Monster", "evade", False):
                return monsterEvading