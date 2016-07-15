'''
TODO:
- Base class for Character which will be inherited by the Player and Enemy class
- Different types of Players and Enemies
- Range of damages instead of a fixed number for different attacks
- An inventory for the Player which can store items that can be used later on.

'''

import random

damages = {"Punch": 20, "Kick": 40, "Fire": 50, "Magic": 30}
prompt = "> "

# Represent the player
class Player:
    moves = {1: "Up", 2: "Down", 3: "Left", 4: "Right"}
    attacks = {1: "Punch", 2: "Kick", 3: "Fire", 4: "Magic"}

    def __init__(self, health):
        self.health = health

    def print_health(self):
        print "Player Health: %d" % self.health

    def move(self):
        print "Choose a direction:"
        for key in self.moves:
            print "%d. %s" % (key, self.moves[key])
        user_dir = int(raw_input(prompt))
        encounter = random.choice(self.moves.keys())
        if user_dir == encounter:
            print "You encountered an enemy!"
            return True
        else:
            print "You found nothing. Keep moving."
            return False

    def attack(self):
        print "Choose an attack:"
        for key in self.attacks:
            print "%d. %s" % (key, self.attacks[key])
        chosen = int(raw_input(prompt))
        attack = self.attacks[chosen]
        damage = damages[attack]
        print "You used %s and did %d damage!" % (attack, damage)
        return damage

    def take_damage(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage


# Represent the enemy
class Enemy:

    def __init__(self, health):
        self.health = health

    def print_health(self):
        print "Enemy Health: %d" % self.health

    def attack(self):
        attack = random.choice(damages.keys())
        damage = damages[attack]
        print "The enemy used %s and did %d damage!" % (attack, damage)
        return damage

    def take_damage(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage


# create a player instance with full health
player = Player(100)

# create an enemy instance with full health
enemy = Enemy(100)

while 1:
    encountered = player.move()

    if encountered:
        while player.health > 0 and enemy.health > 0:
            # player attacks
            enemy.take_damage(player.attack())

            # enemy attacks
            player.take_damage(enemy.attack())

            player.print_health()
            enemy.print_health()

        if player.health == 0:
            print "You lost the battle. Thank Your For Playing"
            raise SystemExit
        else:
            print "The enemy lost! You may continue..."
            continue
