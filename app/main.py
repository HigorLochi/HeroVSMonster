from app.core.Match import Match

from app.entities.Hero import Hero
from app.entities.Monster import Monster

def main():
    hero = Hero()
    monster = Monster()

    match = Match(hero, monster)

    while not match.isFinished():
        match.round()

    match.printWinner()

main()