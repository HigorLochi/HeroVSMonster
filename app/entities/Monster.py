from app.entities.Entity import Entity

class Monster(Entity):
    name = "Monster"
    maximumLife = 200
    life = 200
    minimumDamage = 5
    maximumDamage = 15
    criticalRate = 20