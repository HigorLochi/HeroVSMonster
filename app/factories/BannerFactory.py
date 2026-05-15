from app.variables.banners import *

class BannerFactory:
    def create(banner):
        match banner:
            case 1:
                return heroAttack
            case 2:
                return heroCritical
            case 3:
                return monsterAttack
            case 4:
                return monsterCritical