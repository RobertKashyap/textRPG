from classes.game import Person, bcolors

magic = [{'name':'Fire','cost':10,'dmg':60},
         {'name':'Thunder','cost':10,'dmg':80},
         {'name':'Blizzard','cost':10,'dmg':60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)

while running:
    print('=========================')
    player.choose_action()
    choice = input('Choose an action :')
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked the enemy with',dmg,' points--Enemy hp =',enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy attackked for ',enemy_dmg,' points--Player hp =',player.get_hp())
