from abc import ABC
import random
import math

class Entity(ABC):
    criticalDamage = 20
    lifebarLength = 20
    isDefending = False
    isEvading = False

    def resetState(self):
        self.isDefending = False
        self.isEvading = False

    def attack(self, entityToBeAttacked):
        critical = False
        totalDamage = self.getDamage()

        if(random.randint(0,100) <= self.getCriticalRate()):
            totalDamage = totalDamage + self.criticalDamage
            critical = True
            
        if(entityToBeAttacked.isEntityDefending()):
            totalDamage = totalDamage - (totalDamage / 100 * entityToBeAttacked.getDefencePercentage())
        elif(entityToBeAttacked.isEntityEvading() and random.randint(0,100) <= entityToBeAttacked.getEvasionChance()):
            totalDamage = 0;

        entityToBeAttacked.setLife(entityToBeAttacked.getLife() - totalDamage)

        return {"totalDamage": totalDamage, "critical": critical}

    def defend(self):
        self.isDefending = True

    def evade(self):
        self.isEvading = True

    def printLifeBar(self):
        segmentsCount = math.ceil(self.lifebarLength * self.getLifePercentage() / 100)
        lifeBar = "\n["

        for i in  range(self.lifebarLength):
            if i < segmentsCount:
                lifeBar = lifeBar + '='
            else:
                lifeBar = lifeBar + ' '
        
        print(self.name + "'s Lifebar: " + lifeBar + "]\n")

    def getName(self):
        return self.name;

    def getLife(self):
        return self.life;

    def getLifePercentage(self):
        return self.life * 100 / self.maximumLife

    def getDamage(self):
        return random.randint(self.minimumDamage, self.maximumDamage);

    def getCriticalRate(self):
        return self.criticalRate;

    def isEntityDefending(self):
        return self.isDefending;

    def getDefencePercentage(self):
        return self.defencePercentage;

    def isEntityEvading(self):
        return self.isEvading;

    def getEvasionChance(self):
        return self.evasionChance;

    def setLife(self, life):
        self.life = life
    