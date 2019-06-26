# Reid Harry
# 03/22/2019
# This program uses the Superhero class to tell a story about Cyborg Man.


class Superhero:
        # Superhero class represents the facts related to a superhero.
    def __init__(self, name="", strengthPts=0, villian="", weakness="", moveName=""):
        # Create a new Superhero with a name and other attributes
        self.name = name
        self.strengthPts = strengthPts
        self.villian = villian
        self.weakness = weakness
        self.moveName = moveName

    def addStrengthPts(self, points):
        # Adds points to the superhero's strength.
        self.strengthPts = self.strengthPts + points

    def useFinishingMove(self):
        # Performs a finishing move and adds 50 points
        print(self.name + " used his finishing move: " + self.moveName +
              "! " + self.villian + " was defeated once again! ")
        self.addStrengthPts(50)


def main():
    CyborgMan = Superhero("Cyborg Man", 100, "Super Soaker",
                          "Water", "Autonomous Annihilation")
    print("Get ready for the greatest superhero to ever exist.")
    print(CyborgMan.name + " is his name and kicking villian butt is his game. Speaking of villians, his greatest enemy is " + CyborgMan.villian + ". Just yesterday " + CyborgMan.name +
          " had an intense battle with " + CyborgMan.villian + ". His strength number at the beginning of the battle was " + str(CyborgMan.strengthPts) + ". He ended the battle in signature fashion. ")
    CyborgMan.useFinishingMove()
    print(CyborgMan.name + " now has a strength number of " +
          str(CyborgMan.strengthPts) + "!")


main()
