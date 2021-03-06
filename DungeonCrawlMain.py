from random import random
from math import ceil
Loot = 0
Health = 10
Monster = False
TotalLoot = 0
PlayerDamadge = 0
WeaponPower = 10
print( '______                                     ______                               __   _____  ' )
print( '|  _  \                                    | ___ \                             /  | |  _  | ' )
print( '| | | |_   _ _ __   __ _  ___  ___  _ __   | |_/ /___   __ _ _ __ ___   __   __`| | | |/| | ' )
print( '| | | | | | |  _ \ / _` |/ _ \/ _ \|  _ \  |    // _ \ / _` |  _ ` _ \  \ \ / / | | |  /| | ' )
print( '| |/ /| |_| | | | | (_| |  __/ (_) | | | | | |\ \ (_) | (_| | | | | | |  \ V / _| |_\ |_/ / ' )
print( '|___/  \__,_|_| |_|\__, |\___|\___/|_| |_| \_| \_\___/ \__,_|_| |_| |_|   \_/  \___(_)___/  ' )
print( '                    __/ |                                                                   ' )
print( '                   |___/                                                                    ' )
print('A Generic Dungeon Game By Natelolzzz')
print( 'Type Help For Help')
    
while True:
    Command = input('> ')
    if Command == 'Help' :
        print( 'Welcome To The Help Menu!' )
        print( 'Here Are Commands The Game Uses:')
        print( 'Restore Health')
        print( 'To The Next Room!')
        print( 'Fight')
        print( 'Show Stats')
        print( 'Shop')
        print( 'If This Is Your First Time, Use To The Next Room!')
    
    if Command == 'To The Next Room!' and Monster == True:
        print('You Cant Leave, Theres A Monster!')
    
    if Command == 'To The Next Room!' and Monster != True:
        Walls = ceil(random()*10)
        if Walls == 1 :
            print('The Walls Are Stone')
        if Walls == 2 :
            print('The Walls Are Dirt')
        if Walls == 3 :
            print('The Walls Are Wood')
        if Walls == 4 :
            print('The Walls Are Too Mossy To See')
        if Walls == 5 :
            print('The Walls are Stone, Held Up By Beams')
        if Walls == 6 :
            print('The Walls Are Dirt, Held Up By Beams')
        if Walls == 7 :
            print('The Walls Are Wood, Held Up By Beams')
        if Walls == 8 :
            print('The Walls Are Too Mossy To See But Are Held Up With Beams')
        if Walls == 9 or Walls == 10:
            print('You Arent Paying Attention To The Walls')
        
        MonsterChance = ceil(random()*10)
        Monster = True
        if MonsterChance == 1 or MonsterChance == 2 :
            print('The Monster Is A Skeleton!' )
            MonsterHP = 0.1 * WeaponPower
        if MonsterChance == 3 or MonsterChance == 4 :
            print('The Monster Is A Mimic!')
            MonsterHP = 0.4 * WeaponPower
        if MonsterChance == 5 or MonsterChance == 6:
            print('The Monster Is A Dragon!')
            MonsterHP = 1 * WeaponPower
        if MonsterChance == 7 or MonsterChance == 8 :
            print('The Monster Is A Knight')
            MonsterHP = 0.6 * WeaponPower
        if MonsterChance == 9 or MonsterChance == 10:
            print('The Monster Is A Zombie')
            MonsterHP = 0.2 * WeaponPower
      
    if Command == 'Fight' and Monster == True :
        if ceil(random()*10) >= 5:
            PlayerDamadge = ceil(random()*WeaponPower)
            print('Do',PlayerDamadge, 'Damage')
            MonsterHP = MonsterHP - PlayerDamadge
            if MonsterHP == 0:
                Monster = False
                print('You Killed It!')
                Loot = ceil(random()*10)
                print('Gain ',Loot,' coins!')
                TotalLoot = TotalLoot + Loot
        else :
            print('You Miss')
        
    if Command == 'Fight' and Monster == True :
        Damage = ceil(random()*4)
        print('The Monster Attacks!')
        print('You Take',Damage, 'Damage')
        Health = Health - Damage
        if Health <= 0:
            break
    
    if Command == 'Show Stats' :
        print('Health is',Health)
        print('All Your Loot Is',Loot)
        if Monster == True :
            print('The Monsters Health is',MonsterHP)
    
    if Command == 'Restore Health' :
        print ('Health Up!')
        Health = Health + ceil(random()*10)
        print ('Health Is Now:', Health)
        
    if Command == 'Shop' and Monster == False:
        print('Welcome To My Shop Traveller, May I Interest You In My Wares?')
        print('1: Weapon Upgrade: 10 Gold')
        print('Use Exit To Exit Shop')
        while True:
            Buying = input('What Am I To Buy? > ')
            if Buying == 1 and TotalLoot >= 10:
                print('Excellent Choice')
                WeaponPower = WeaponPower + 1
                TotalLoot = TotalLoot - 10
            elif Buying == 1 and TotalLoot < 10:
                print('You Simply Do Not Have The Money')
            if Buying == 'Exit':
                break
    
    elif Command == 'Shop' and Monster == True:
        print('You Cant, Theres A Monster')

print('Game Over!')
