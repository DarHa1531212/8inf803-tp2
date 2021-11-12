class Creature:
    def __init__(self, name, team, health, speed, armor, weapons, position):
        self.name = name
        self.team = team
        self.health = health
        self.speed = speed
        self.armor = armor
        self.weapons = weapons
        self.position = position

    def play_turn(self, creatures):
        creatures.remove(self)
        # creature.remove retirer les creatures qui sont dans le meme equipe
