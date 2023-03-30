
class Hero():
    """ Class to Create Hero for our Game"""
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """ Print all parameters of this Hero"""
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """ Upgrade Level of Hero"""
        self.level += 1

    def move(self):
        """ Start moving hero"""
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health

# ---------------------------------------------------------------------


class SuperHero(Hero):
    """ Class to Crete SUper Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super Hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """ Use magic"""
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " Health is " + str(self.health) +
                       " Magic is: " + str(self.magic)).title()
        print(discription)
        

myhero1 = Hero("Vurdalak", 5, "Orc")
myhero2 = Hero("Alexander", 4, "Human")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()

myhero = Hero("Vurdalak", 4, "Orc")
mysuperhero = SuperHero("Moisey", 10, "Human", 5)

myhero.show_hero()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()

mysuperhero.magic = 10
mysuperhero.show_hero()