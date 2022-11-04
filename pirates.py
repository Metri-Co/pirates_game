class Weapon():
    def __init__(self, name, damage, scope):
        if scope != 'short' and scope != 'long':
            print("scope must be 'short' or 'long' strings")

        if damage < 1:
            print("Damage can not be equal or less than 0")

        self.name = name
        self.damage = damage
        self.scope = scope


class Pirate():
    boat_life = 200

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, enemy):
        valid_attack = True

        if self.weapon.scope == 'short' and enemy.position == 'far':
            valid_attack = False
            print(f"The enemy was not in attack range!! {self.name} has missed the attack")

        if valid_attack == True:
            enemy.hit(self.weapon.damage)
            print(f"Pirate {self.name} has attacked {enemy.name}!!!")

    @classmethod
    def hit(cls, pirate, damage):

        Pirate.boat_life -= damage

        name = pirate.name
        weapon = pirate.weapon

        return cls(name, weapon)


class Enemy():
    def __init__(self, name, health, position, min_damage, max_damage):
        self.name = name
        self.health = health
        self.position = position
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self, pirate):
        import numpy as np
        critical = [1, 5, 10, 20]
        damage_dealt = np.random.randint(0, 21)

        if damage_dealt in critical:
            damage_dealt = self.max_damage
            print(f"Oh no! {self.name} has attacked {pirate.name} with a critical hit")

        else:
            damage_dealt = self.min_damage
            print(f"Oh no! {self.name} has attacked {pirate.name}")

        Pirate.hit(pirate=pirate, damage=damage_dealt)

    def move(self):
        import numpy as np
        valid = [1, 5, 15]
        movement = np.random.randint(0, 21)

        if movement in valid:
            if self.position == 'near':
                self.position = 'far'
            elif self.position == 'far':
                self.position = 'near'
            print(f"The enemy {self.name} has change his position! He must wait for his next turn to make a move")

    def hit(self, damage):
        self.health -= damage


def restart_battle(enemy_list):
    Pirate.boat_life = 200

    for enemy in enemy_list:
        enemy.health = 25

    print("\nThe boat has sunk!!! All stats will be reset and the battle will start again. Good luck Pyrate!!\n")
    return enemy_list


def start_battle(heroes, villains):
    import numpy as np
    import time

    pyrates = heroes.copy()
    enemies = villains.copy()
    count = 0

    # initialize the game; the conditions are 1) the enemies are defeated, 2) the boat life is higher than 0, else, restart battle with `restart_battle` function
    while len(enemies) > 0:
        # chek the number of enemies in the list and select the enemy for being attacked
        enemy = enemies[count]
        print(f"The actual enemy is {enemy.name}, start the battle Pyrates!!!")
        print("----------------------------------------------------------------")
        time.sleep(2)

        print("\nPyrates are attacking!")
        time.sleep(2)
        # Start with pyrates attack
        for pyrate in pyrates:
            pyrate.attack(enemy)

        # check is the enemy health is higher than 0
        if enemy.health > 0:
            print(f"The enemy {enemy.name} has {enemy.health} remaining health!!")
            time.sleep(2)

        # check the life of the enemy, if <= 0, drop the enemy from the list
        elif enemy.health <= 0:
            enemies.remove(enemy)
            print(f"The enemy {enemy.name} has been defeated!!")
            print("--------------------------------------------")
            time.sleep(2)

        print("\nEnemies are attacking!")
        time.sleep(2)
        for monster in enemies:
            # randomly decide if attack or move
            action = np.random.randint(0, 2)
            pyrate_attacked = np.random.randint(0, 3)  # randomly select a pyrate index
            if action == 0:
                monster.move()
            elif action == 1:
                monster.attack(pyrates[pyrate_attacked])

        # restart game if the boat healts is equal or below 0
        if pyrates[count].boat_life <= 0:
            villains = restart_battle(villains)
            return start_battle(heroes, villains)

        # print the remaining boat life if its higher than 0
        elif pyrates[count].boat_life > 0:
            print(f"\nThe boat has {Pirate.boat_life} life remaining")
            print("--------------------------------------------")
            time.sleep(2)


    return print("\n------ Congrats, the Pyrates won the battle!! ------")
