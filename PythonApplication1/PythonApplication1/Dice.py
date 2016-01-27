import random

def Trow_dice():
    diceList = [1,2,3,4,5,6]
    dice = random.choice(diceList)
    diceImglist = ["Dice1.png","Dice2.png","Dice3.png","Dice4.png","Dice5.png","Dice6.png"]
    diceImg = diceImglist[dice-1]
    return dice,diceImg


for i in range(6):
    dice = Trow_dice()
    diceImg = dice[1]
    dice = dice[0]
    print (dice)
    print (diceImg)
    
##functie Trow_dice() opnieuw uitvoeren voor player B 
# DIT IS VOOR DE SPOTFIGHT !!! 
#attack_b= 0

#if dice == 1:
#    attack_b += player_b.dice1
#elif dice == 2:
#    attack_b += player_b.dice2
#elif dice == 3:
#    attack_b += player_b.dice3
#elif dice == 4:
#    attack_b += player_b.dice4
#elif dice == 5:
#    attack_b += player_b.dice5
#elif dice == 6:
#    attack_b += player_b.dice6

#attack_a= 0

#if dice == 1:
#    attack_a += player_a.dice1
#elif dice == 2:
#    attack_a += player_a.dice2
#elif dice == 3:
#    attack_a += player_a.dice3
#elif dice == 4:
#    attack_a += player_a.dice4
#elif dice == 5:
#    attack_a += player_a.dice5
#elif dice == 6:
#    attack_a += player_a.dice6



#attack_a.conditionPoints -= 3 
#attack_b.conditionPoints -= 3

#if player_a.conditionPoints > 0 and player_b.conditionPoints > 0:
#    if attack_a => attack_b:
#        totalattack = attack_a - attack_b
#        player_b.hitPoints -= totalattack
#    else: 
#        totalattack = attack_b - attack_a
#        player_a.hitPoints -= totalattack
#elif player_a.conditionPoints > 0 and player_b.conditionPoints < 1:
#    player_b.hitPoints -= attack_a
#elif player_a.conditionPoints < 1 and player_b.conditionPoints > 0:
#    player_a.hitPoints -= attack_a


# DIT IS VOOR DE CORNERFIGHT!!! 


#attack_b= 2

#if dice == 1:
#    attack_b += player_b.dice1
#elif dice == 2:
#    attack_b += player_b.dice2
#elif dice == 3:
#    attack_b += player_b.dice3
#elif dice == 4:
#    attack_b += player_b.dice4
#elif dice == 5:
#    attack_b += player_b.dice5
#elif dice == 6:
#    attack_b += player_b.dice6

#attack_a= 0

#if dice == 1:
#    attack_a += player_a.dice1
#elif dice == 2:
#    attack_a += player_a.dice2
#elif dice == 3:
#    attack_a += player_a.dice3
#elif dice == 4:
#    attack_a += player_a.dice4
#elif dice == 5:
#    attack_a += player_a.dice5
#elif dice == 6:
#    attack_a += player_a.dice6



#attack_a.conditionPoints -= 3 
#attack_b.conditionPoints -= 3

#if player_a.conditionPoints > 0 and player_b.conditionPoints > 0:
#    if attack_a => attack_b:
#        totalattack = attack_a - attack_b
#        player_b.hitPoints -= totalattack
#    else: 
#        totalattack = attack_b - attack_a
#        player_a.hitPoints -= totalattack
#elif player_a.conditionPoints > 0 and player_b.conditionPoints < 1:
#    player_b.hitPoints -= attack_a
#elif player_a.conditionPoints < 1 and player_b.conditionPoints > 0:
#    player_a.hitPoints -= attack_a
