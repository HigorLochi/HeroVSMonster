import random

from app.factories.BannerFactory import BannerFactory
from app.handlers.PlayerInputHandler import PlayerInputHandler
from app.variables.entityActions import entityActions

class Match():
    roundsCount = 0

    def __init__(self, leftEntity, righEntity):
        self.leftEntity = leftEntity
        self.righEntity = righEntity

    def round(self):
        playerInputHandler = PlayerInputHandler()

        self.incrementRoundCounter()
        self.printRound()

        self.leftEntity.resetState()
        self.righEntity.resetState()

        self.leftEntity.printLifeBar()
        self.righEntity.printLifeBar()

        playerAction = playerInputHandler.getAction()
        playerActionMethod = getattr(self.leftEntity, playerAction)
        if(playerAction == "attack"):
            leftAttackData = playerActionMethod(self.righEntity)

            print("Damage Dealt: " + str(leftAttackData['totalDamage']))
            print(BannerFactory.create(self.leftEntity.getName(), playerAction, leftAttackData["critical"]))
        else:
            playerActionMethod()
            print(BannerFactory.create(self.leftEntity.getName(), playerAction))

        monsterAction = entityActions[random.randint(0, len(entityActions) - 1)]
        print("Monster Action: " + monsterAction)

        monsterActionMethod = getattr(self.righEntity, monsterAction)
        if(monsterAction == "attack"):
            rightAttackData = monsterActionMethod(self.leftEntity)
            
            print("Damage Received: " + str(rightAttackData['totalDamage']))
            print(BannerFactory.create(self.righEntity.getName(), monsterAction, rightAttackData["critical"]))
        else:
            monsterActionMethod()
            print(BannerFactory.create(self.righEntity.getName(), monsterAction))

    def isFinished(self):
        if(self.leftEntity.getLife() <= 0 or self.righEntity.getLife() <= 0):
            return True
        else:
            return False
        
    def printRound(self):
        print("\n========================= Round " + str(self.roundsCount) + " =========================\n")

    def printWinner(self):
        print(self.getWinner().getName() + " wins!")

    def getWinner(self):
        if(self.leftEntity.getLife() <= 0): 
            return self.righEntity
        else:
            return self.leftEntity
        
    def incrementRoundCounter(self):
        self.roundsCount = self.roundsCount + 1