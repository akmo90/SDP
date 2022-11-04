import random
#factory 
def createhero():
    print("Create your hero!")
    selection = input("Write your name: ")
    health = input("Write your health:")
    strength = input("Write your strength:")
    defence = input("Write your defence:")
    magic = input("Write your magic:")
    
    print(selection, "start adventure text game")
    print("\n",selection,"health - ", health,"\n", selection,"strength - ",strength,"\n",selection,"defence",defence,"\n",selection,"magic - ",magic) 

def vybor():
    print ("Select your hero!")
    selection = input("1. Create your hero \n2. Select your hero")
    if selection == "1":
       createhero()
    elif selection == "2":
        heroselect()
    else:
        print("Only press 1, 2 ")
        heroselect()


    
#Hero Classes
class warrior (object):
    health = 50
    strength = 10
    defence = 10
    magic = 1

class wizard (object):
    health = 125
    strength = 7
    defence = 7
    magic = 10

class elf (object):
    health = 100
    strength = 5
    defence = 10
    magic = 7

# Enemy Classes

class goblin (object):
    name = "Goblin"
    health = 25
    strength = 4
    defence = 2
    loot = random.randint(0,2)

class slime (object):
    name = "Slime"
    health = 15
    strength = 1
    defence = 3
    loot = random.randint(0,2)

class snake (object):
    name = "Snake"
    health = 40
    strength = 5
    defence = 4
    loot = random.randint(0,2)

class boss(object):
    name = "boss"
    health = 150
    strength = 50
    defence = 50
#Observer
def gameOver(character, score):
    if character.health < 1:
        print("You have no health left")
        print("Thanks for playing...")
        print("You have scored...", score)
        
        writeScore(score)

        file=open("score.txt","r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])

        exit()
        

def writeScore(score):
    file = open("score.txt","a")
    name = input("Type your name...")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()

#Strategy
def heroselect():
    print ("Select your hero!")
    selection = input("1. Warrior \n2. Wizard \n3. Elf \n")
    if selection == "1":
        character = warrior
        print ("You have selected the warrior...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "2":
        character = wizard
        print ("You have selected the wizard...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "3":
        character = elf
        print ("You have selected the elf...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()

def enemyselect(goblin,bat,troll):
    enemyList = [goblin,bat,troll]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, character):
    if lootDrop == "potion":
        character.health = character.health + 20
        print ("you drink the potion, increasing your health by 20!")
        print ("Your health is now", character.health)
        return character

    elif lootDrop == "sword":
        character.strength = character.strength + 3
        print ("you swap your sword for the newer, much sharper one!")
        print ("Your strength has been increased by 3")
        print ("your new strength is now", character.strength)
        return character

    elif lootDrop == "shield":
        character.defence = character.defence + 5
        print ("you swap your shield for the newer, much stronger one!")
        print ("Your defence has been increased by 5")
        print ("your new strength is now", character.defence)
        return character

    elif lootDrop == "poison":
        character.defence = character.health - 10
        print ("You just tasted the poison now your health will get worse!")
        print ("Your defence has been deacreased by 3")
        print ("your health is now", character.defence)
        return character

    
    
def battlestate(score):
    enemy = enemyselect(goblin,snake,slime)
    print( enemy.name, "has appeared!")
    print ("you have 3 options...")
    while enemy.health > 0 :
        choice = input("1. Sword\n2. Magic \n3. RUN!\n")

        if choice == "1":
            print ("You swing your sword, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                    

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Snake":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Slime":
                        enemy.health = 30
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("Your sword slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "2":
            print ("You cast a spell, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.magic
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Snake":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Slime":
                        enemy.health = 30
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("You slip when casting your spell, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "3":
            print("you try to run....")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("you got away unscratched!")
                break
            else:
                print ("You try to run but slip and fall")
                print ("You try to defend but cannot, the enemy hits you for full damage...")
                character.health = character.health - enemy.strength
                print ("Your health is now", character.health)
                gameOver(character, score)

        else:
            print ("number not allowed, please only type 1, 2 or 3...")
        

def BossBattleState(score):
    enemy = boss
    


vybor()
score = 0
character = heroselect()
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
print (score)
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
writeScore(score)
