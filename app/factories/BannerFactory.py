from app.variables.banners import *

class BannerFactory:
    def create(entity, critical):
        match (entity, critical):
            case ("Hero", False):
                return heroAttack
            case ("Hero", True):
                return heroCritical
            case ("Monster", False):
                return monsterAttack
            case ("Monster", True):
                return monsterCritical