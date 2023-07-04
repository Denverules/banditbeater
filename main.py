import random

elements = ['fire', 'water','earth','ice','air'
            ]
class Bandit:
    def __int__(self,healthb,speedb,defenseb,swordskillb,elskillb,elementb,drops):
        self.elementb = elementb
        self.healthb = healthb
        self.speedb = speedb
        self.defenseb = defenseb
        self.swordskillb = swordskillb
        self.elskillb = elskillb
        self.drops = drops
def banditgen(diff):
    global enemy
    if diff == 0:
        enemy = Bandit()
        enemy.healthb = random.randint(50,100)
        enemy.speedb = random.randint(5,15)
        enemy.elementb = random.choice(elements)
        enemy.defenseb = random.randint(5,10)
        enemy.swordskillb = random.randint(5,15)
        enemy.elskillb = random.randint(5,15)
        enemy.drops = random.randint(10, 50)
    elif diff == 1:
        enemy = Bandit
        enemy.healthb = random.randint(80, 120)
        enemy.speedb = random.randint(20, 30)
        enemy.elementb = random.choice(elements)
        enemy.defenseb = random.randint(20, 25)
        enemy.swordskillb = random.randint(20, 30)
        enemy.elskillb = random.randint(20, 30)
        enemy.drops = random.randint(60, 100)
    elif diff == 2:
        enemy = Bandit
        enemy.healthb = random.randint(180, 220)
        enemy.speedb = random.randint(35, 35)
        enemy.elementb = random.choice(elements)
        enemy.defenseb = random.randint(35, 40)
        enemy.swordskillb = random.randint(35, 40)
        enemy.elskillb = random.randint(35, 45)
        enemy.drops = random.randint(80, 150)
    elif diff == 3:
        enemy = Bandit
        enemy.healthb = random.randint(220, 260)
        enemy.speedb = random.randint(45,55)
        enemy.elementb = random.choice(elements)
        enemy.defenseb = random.randint(45, 55)
        enemy.swordskillb = random.randint(45, 55)
        enemy.elskillb = random.randint(45, 55)
        enemy.drops = random.randint(120, 200)
    elif diff == 4:
        enemy = Bandit
        enemy.healthb = random.randint(50, 100)
        enemy.speedb = random.randint(55, 75)
        enemy.elementb = random.choice(elements)
        enemy.defenseb = random.randint(55, 65)
        enemy.swordskillb = random.randint(55, 80)
        enemy.elskillb = random.randint(45, 90)
        enemy.drops = random.randint(190, 230)



def fight():
    global maxhealth,yourelem,swordskill,defense,coins,robbed,banditdefeated

    health = maxhealth
    round=1
    escape = ''
    print('the bandits element is',enemy.elementb)
    while enemy.healthb>=0 and health >=0:
        print('round',round)
        if enemy.speedb> speed:
            damagedone=attack(enemy.swordskillb,enemy.elskillb,defense,enemy.elementb,yourelem)
            health -= damagedone
            print('the bandit was faster it attacked you for',damagedone,'. your health is now',health)
            if health>0:
                damagedone = attack(swordskill,elskill,enemy.defenseb,yourelem,enemy.elementb)
                print('you attacked the bandit for', damagedone, ". the bandit's health is now", health)
                enemy.healthb-=damagedone
        else:
            damagedone = attack(swordskill, elskill, enemy.defenseb, yourelem, enemy.elementb)
            enemy.healthb-= damagedone
            print('you were faster than the bandit you attacked it for',damagedone,"the bandit's health is now",enemy.healthb)
            if enemy.healthb>0:
                damagedone = attack(enemy.swordskillb, enemy.elskillb, defense, enemy.elementb, yourelem)
                health -= damagedone
                print('the bandit attacked you for', damagedone, '. your health is now', health)
        if health <= 0:
            print('the bandits robbed you')
            coins = coins // 2
            robbed+=1
            break
        if enemy.healthb <= 0 and banditdefeated<10:
            print('you won the fight you got',enemy.drops,'coins')
            coins += enemy.drops
            banditdefeated+=1
            break
        elif enemy.healthb <= 0 and banditdefeated>=10:
            print('you beat the bossfight and freed the village you have won the game')
            quit()

        if escape == '':
            escape=input('would you like to try to run away?yes/no').lower()
        if escape == 'yes' and speed>enemy.speedb:
            print('you ran away sucsessfully')
            break
        elif escape =='yes' and speed<enemy.speedb:
            print('you couldnt run away the fight continues')
        else:
            print('the fight continues')
        round+=1
def hunt():
    global maxhealth, enemy,speed,defense,swordskill,elskill,difficulty,coins,robbed,banditdefeated
    health = maxhealth
    armors = {'cloth':0,'leather':5,'chain':15,'iron':20}
    swords = {'stick':0,'wooden':5,'stone':15,'longsword':20}
    for i in swords:
        if i == sword:
            swordskill += swords.get(i)
    for j in armors:
        if j == armor:
            defense += armors.get(j)
    difficulty = int(input('what level bandits would you like to hunt from 0-4'))
    if banditdefeated< 10:
        banditgen(difficulty)
        fight()
    else:
        print('you are going to fight the boss bandit')
        enemy = Bandit()
        enemy.healthb = 1000
        enemy.speedb = 40
        enemy.elementb = random.choice(elements)
        enemy.defenseb = 70
        enemy.swordskillb = 50
        enemy.elskillb = 50
        enemy.drops = 1000
        fight()

def shop(coin):
    global sword,armor,intel,coins
    discount = 1 - intel/1000
    buy = 'none'
    print('you have',coin,'coins')
    if coin<(100 * discount):
        print('you do not have enough money to buy anything')
        pass
    if (100 * discount) <= coin <= (200 * discount):
        buy=input('would you like to buy wooden sword or leather armor').lower()
    if (200 * discount) <= coin <= (300 * discount):
        buy=input('would you like to buy chain armor or stone sword').lower()
    if coin>= (300* discount):
        buy=input('would you like to buy iron armor or longsword').lower()
    if buy == 'wooden sword' and sword != 'wooden' and sword !='stone' and sword !='long':
        coins-= (100* discount)
        sword = 'wooden'
        print('you have bought wooden sword succesfully')
    elif buy == 'stone sword' and sword !='stone' and sword !='long':
        coins-= (200* discount)
        sword = 'stone'
        print('you have bought stone sword succesfully')
    elif buy == 'longsword' and sword !='longsword':
        coins-= (300* discount)
        sword = 'longsword'
        print('you have bought longsword succesfully')
    elif buy != 'none':
        print('you have a better/same sword')
    if buy == 'leather armor' and armor != 'leather' and armor !='chain' and armor !='iron' :
        coins-= (100* discount)
        armor = 'leather'
        print('you have bought leather armor succesfully')
    elif buy == 'chain armor' and armor !='chain' and armor !='iron' :
        coins-= (200* discount)
        armor = 'chain'
        print('you have bought chain armor succesfully')
    elif buy == 'iron armor' and armor !='iron' :
        coins-= (300* discount)
        armor = 'iron'
        print('you have bought iron armor succesfully')
    elif buy!='none' or 'sword' not in buy :
        print('you have better/same armor')
def play():
    global difficulty,robbed
    quitting = False

    while not quitting:

        action = input('what would you like to do next, hunt bandits, train, shop or quit').lower()
        if action == 'quit':
            print('game over')
            quitting = True
        elif action == 'train':
            train = input(
                'what would you like to train? max health,speed defense sword skill element skill or intelligence').lower()
            training(train)
            print('your current stats are', maxhealth, 'max health,', speed, 'speed,', defense, 'defense,', swordskill,
                  'sword skill,', elskill, 'element skill', intel, 'intelligence')
        elif action == 'shop':
            shop(coins)
        elif action =='hunt bandits':

            hunt()
        if robbed >= 3:
            print('game over you lose')
            quit()

def training(stat):
    global maxhealth,speed,defense,swordskill,elskill,intel
    max = True
    if stat == 'max health' and maxhealth != 500:
        increase = random.randint(10,20)
        if maxhealth + increase >= 500:
            maxhealth = 500
            max = True
        else:
            max = False
            maxhealth+= increase
    if stat == 'speed' and speed != 100:
        increase = random.randint(5,10)
        if speed + increase >= 100:
            speed = 100
            max = True
        else:
            speed+= increase
            max = False
    if stat == 'defense' and defense != 100:
        increase = random.randint(5, 10)
        if defense + increase >= 100:
            defense = 100
            max = True
        else:
            defense += increase
            max = False
    if stat == 'sword skill' and swordskill != 100:
        increase = random.randint(5, 10)
        if swordskill + increase >= 100:
            swordskill = 100
            max = True
        else:
            swordskill += increase
            max = False
    if stat == 'element skill' and elskill != 100:
        increase = random.randint(5,10)
        if elskill + increase >= 100:
            elskill = 100
            max = True
        else:
            elskill+= increase
            max = False
    if stat == 'intelligence' and intel != 100:
        increase = random.randint(10,20)
        if intel + increase >= 200:
            intel = 200
            max = True
        else:
            intel+= increase
            max = False
    if max == True:
        print('statistic is at max')
    else:
        print('training successful',stat,'increased by',increase)
def attack(swords,elementsk,defstat,elementatk,elementdf,effective=0,damage=1):
    atk=1
    df =1
    if elementatk == 'fire' and elementdf == 'water':
        atk = 0
    elif elementatk == 'fire' and elementdf == 'earth':
        atk = 0
    elif elementatk == 'fire' and elementdf == 'ice':
        atk = 2
    elif elementatk == 'fire' and elementdf == 'air':
        atk = 2
    elif elementatk == 'water' and elementdf == 'fire':
        atk = 2
    elif elementatk == 'water' and elementdf == 'earth':
        atk = 2
    elif elementatk == 'water' and elementdf == 'ice':
        atk = 0
    elif elementatk == 'water' and elementdf == 'air':
        atk = 0
    elif elementatk == 'earth' and elementdf == 'ice':
        atk = 0
    elif elementatk == 'earth' and elementdf == 'water':
        atk = 0
    elif elementatk == 'earth' and elementdf == 'fire':
        atk = 2
    elif elementatk == 'earth' and elementdf == 'air':
        atk = 2
    elif elementatk == 'air' and elementdf == 'water':
        atk = 2
    elif elementatk == 'air' and elementdf == 'earth':
        atk = 0
    elif elementatk == 'air' and elementdf == 'ice':
        atk = 2
    elif elementatk == 'air' and elementdf == 'fire':
        atk = 0
    elif elementatk == 'ice' and elementdf == 'air':
        atk = 0
    elif elementatk == 'ice' and elementdf == 'earth':
        atk = 2
    elif elementatk == 'ice' and elementdf == 'water':
        atk = 2
    elif elementatk == 'ice' and elementdf == 'fire':
        atk = 0
    damage += swords + elementsk /2
    if damage - (defstat/2) > 0:
        damage -= defstat/2
    else:
        damage = 1
    if atk> df:
        damage *= 1.25
        effective = 1
    elif df>atk:
        damage *=0.75
        effective = 2
    if effective == 1:
        print('attack was super effective')
    elif effective == 2:
        print('attack was not very effective')
    return(damage)

yourelem=random.choice(elements)
maxhealth = 0
speed = 0
defense = 0
swordskill = 0
elskill = 0
intel = 0
difficulty = 0
def statgen():
    global maxhealth
    global speed
    global defense
    global swordskill
    global elskill
    global intel
    global difficulty
    difficulty = random.randint(0, 4)
    if difficulty == 0:
        maxhealth = 100
        speed = 10
        defense = 10
        swordskill = 10
        elskill = 10
        intel = 40
    elif difficulty == 1:
        maxhealth = 150
        speed = 25
        defense = 25
        swordskill = 25
        elskill = 25
        intel = 60
    elif difficulty ==2:
        maxhealth = 200
        speed = 40
        defense = 40
        swordskill = 40
        elskill = 40
        intel = 80
    elif difficulty ==3:
        maxhealth = 250
        speed = 50
        defense = 50
        swordskill = 50
        elskill = 50
        intel = 100
    elif difficulty ==4:
        maxhealth = 300
        speed = 65
        defense = 65
        swordskill = 65
        elskill = 65
        intel = 120
statgen()

print('you are just born in a village,your village has been oppressed by bandits'
      ' stealing from you, in order to defeat them you must first'
      'fight 10 bandits then you can fight their leader to free your village'
      ', these are your stats', maxhealth, 'maxhealth,', speed, 'speed,', defense, 'defense,', swordskill,
      'sword skill,', elskill,'elemental skill and', intel,'intelligence and your element is', yourelem)
sword='stick'
armor = 'cloth'
banditdefeated =0
robbed = 0
coins = 0
play()
