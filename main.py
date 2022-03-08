import random

try:
    hero_hp = int(input("how many hp does the hero have?"))
    dragon_hp = int(input("how many hp does the dragon have?"))
    hero_max_dmg = int(input("what is the maximum damage the hero can cause?"))
    dragon_max_dmg = int(input("what is the maximum damage the dragon can cause?"))
    print('Thank you for your input\n')
except:
    print('Input was not correct, hardcoded values will be used for this game: \n')
    hero_hp = 50
    dragon_hp = 100
    hero_max_dmg = 10
    dragon_max_dmg = 20
finally:
    print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")
    print("The dragon can cause maximum damages of", dragon_max_dmg, ", while the hero can attacks with maximum", hero_max_dmg, '\n')

while dragon_hp > 0 and hero_hp > 0:
    print('Now the dragon attacks!')
    dragon_attack = random.randint(1, dragon_max_dmg)
    hero_hp = hero_hp - dragon_attack
    if hero_hp <= 0:
        print("Unfortunately the dragon killed our hero with a last attack of", dragon_attack, ". RIP sir Bravealot")
        break
    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left", '\n')
    print('Now the hero attacks!')
    hero_attack = random.randint(1, hero_max_dmg)
    dragon_hp = dragon_hp - hero_attack
    if dragon_hp <= 0:
        print("Our valiant hero has slain the dragon, with a final attack of", hero_attack, "!")
        break
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left", '\n')
    input("Round over. The hero is still alive! Let's continue the fight! Press any key to continue:", '\n')
