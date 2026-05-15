from app.entities.Entity import Entity
from app.factories.BannerFactory import BannerFactory
from app.handlers.PlayerInputHandler import PlayerInputHandler

class Match(Entity):
    roundsCount = 0

    def __init__(self, leftEntity, righEntity):
        self.leftEntity = leftEntity
        self.righEntity = righEntity

    def round(self):
        self.incrementRoundCounter()
        self.printRound()

        self.leftEntity.printLifeBar()
        self.righEntity.printLifeBar()

        playerInputHandler = PlayerInputHandler()
        playerAction = playerInputHandler.getAction()
        
        if(playerAction == 1):
            self.leftEntity.attack(self.righEntity)
            print(BannerFactory.create(1))

            self.righEntity.attack(self.leftEntity)
            print(BannerFactory.create(3))
        elif(playerAction == 2):
            self.leftEntity.defend()

    def isFinished(self):
        if(self.leftEntity.getLife() <= 0 or self.righEntity.getLife() <= 0):
            return True
        else:
            return False
        
    def printRound(self):
        print("\n===== Round " + str(self.roundsCount) + " =====\n")

    def printWinner(self):
        print(self.getWinner().getName() + " wins!")

    def getWinner(self):
        if(self.leftEntity.getLife() <= 0): 
            return self.righEntity
        else:
            return self.leftEntity
        
    def incrementRoundCounter(self):
        self.roundsCount = self.roundsCount + 1