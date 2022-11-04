# pirates_game
This was a brief exam of an Udemy course for learning Python. The objective was to create a text-based (without animation) game of pirates against Montsers

The `pirates.py`script contains the `Weapon` `Pirate` and `Enemy` classes, wich are used for starting the game. This script also contains the main function `start battle` to begin the game between pirates and monsters! In the case of Pirates loss the game, the function `restart_battle` will restart all stats of health (both pirates and enemies) and will call again the `start_battle` function. Hence, the pirates always win haha. 

In the `test.py` script is an example of the execution of the game. First you have to create all classes:

```
sword = Weapon(name= 'Espada', damage= 3, scope = 'short')
ax = Weapon(name = 'Hacha', damage = 5, scope = 'short')
bow = Weapon(name = 'Arco', damage = 2, scope = 'long')

torvellino1 = Enemy(name = 'Torvellino 1', health = 25, position = 'near', min_damage=2, max_damage=5)
torvellino2 = Enemy(name = 'Torvellino 2', health = 25, position = 'near', min_damage=4, max_damage=8)
torvellino3 = Enemy(name = 'Torvellino 3', health = 25, position = 'far', min_damage=3, max_damage=5)
torvellino4 = Enemy(name = 'Torvellino 4', health = 25, position = 'far', min_damage=6, max_damage=9)

pyratilla = Pirate(name='Pyratilla', weapon = sword)
pym = Pirate(name = 'Pym', weapon = bow)
pyerce = Pirate(name = 'Pyerce', weapon = ax)
```

Then, create two lists, one of pirates and other of enemies. These lists will be fed into the `start_battle(pirates_list, enemies_list)` to start the game.

```
My_pyrates = [pyratilla, pym, pyerce]
My_enemies = [torvellino1, torvellino2, torvellino3, torvellino4]

pirates.start_battle(My_pyrates, My_enemies)
```

Hope you enjoy it!! It's something really simple and basic, but it was fun for me :D
