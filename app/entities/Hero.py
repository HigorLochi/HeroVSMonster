from app.entities.Entity import Entity

class Hero(Entity):
    name = "Hero"
    maximumLife = 100
    life = 100
    minimumDamage = 1
    maximumDamage = 10
    criticalRate = 40
    defencePercentage = 70
    evasionChance = 80