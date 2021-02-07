#Automate the Boring Stuff: Chapter 6 Practice Project - Zombie Dice Bots
import zombiedice
import random

class TwoBrainZombie:
    #This was the example zombie
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class TwoShotgunZombie:
    #This zombie will roll until it hits 2 shotguns
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):


        diceRollResults = zombiedice.roll() # first roll

        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomZombie:
    #This zombie is completely random
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            if random.randint(0,1) == 0:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class OnetoFourZombie:
    #This zombie will decide to roll 1-4 times at random but stop if it hits 2 shotguns
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        randomroll = random.randint(1,4)
        shotgun = 0
        diceRollResults = zombiedice.roll() # first roll
        count = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll() # roll again
            elif count < randomroll:
                diceRollResults = zombiedice.roll()
                count +=1
            else:
                break

class ShotgunBrainZombie:
    #This zombie will roll as long as it has hit more brains than shotguns
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        brains = 0
        shotgun = 0
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if brains >= shotgun:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


class LoserZombie:
    #This zombie will keep rolling until it hits 3 shotguns and should always lose
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotgun = 0
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 4:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2  Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    TwoBrainZombie(name='Two Brain Stop'),
    TwoShotgunZombie('Two Shotgun Stop'),
    RandomZombie('Random Stop'),
    OnetoFourZombie('1 to 4 Unless 2 Shotgun'),
    ShotgunBrainZombie('Shotgun V Brain'),
    LoserZombie('Loser')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
