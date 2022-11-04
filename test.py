import pirates
from pirates import Weapon, Pirate, Enemy

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

My_pyrates = [pyratilla, pym, pyerce]
My_enemies = [torvellino1, torvellino2, torvellino3, torvellino4]

pirates.start_battle(My_pyrates, My_enemies)