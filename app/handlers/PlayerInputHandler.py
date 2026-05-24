from app.variables.entityActions import entityActions

class PlayerInputHandler:
    def getAction(self):
        print("What will be your action?\n")

        while True:
            for i in range(len(entityActions)):
                print(str(i + 1) + " - " + str(entityActions[i]))

            action = int(input())

            if(action > 0 and action <= len(entityActions)):
                return entityActions[action - 1]
            else:
                print("=== Invalid action ===")