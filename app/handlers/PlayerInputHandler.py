from app.variables.playerActions import playerActions

class PlayerInputHandler:
    def getAction(self):
        print("What will be your action?\n")

        while True:
            for i in range(len(playerActions)):
                print(str(i + 1) + " - " + str(playerActions[i]))

            action = int(input())

            if(action > 0 and action <= len(playerActions)):
                return action
            else:
                print("=== Invalid action ===")