#IMPORTANT NOTES
#Whenever defining FUNCTIONS in the CLASS you always put self as an ARGUMENT
#However when calling FUNTIONS on VARIABLES that you made you do not include self in the FUNCTION ARGUMENT

#create CLASS BattleBot
class BattleBot:
    #create CONSTRUCTOR for CLASS BattleBot that has 5 ARGUMENTS
    #the arguments are bot_health_arg, bot_attack_arg, bot_defense_arg, bot_speed_arg, bot_name_arg
    def __init__(self, bot_health_arg, bot_attack_arg, bot_defense_arg, bot_speed_arg, bot_name_arg):
        #CLASS VARIABLES are created and assign to the ARGUMENTS
        #keywork self shows that these VARIABLES belong to the OBJECT made with this CLASS
        self.health = bot_health_arg
        self.attack_damage = bot_attack_arg
        self.defense = bot_defense_arg
        self.speed = bot_speed_arg
        self.name = bot_name_arg
    
    #CLASS FUNCTION which controls the bot attacks
    #it take opponent as an ARGUMENT which is a battle bot so it has of of the CLASS VARIABLES and CLASS FUNCTIONS
    def attack(self, opponent):
        #FUNCTION take_damage(damage) called on OBJECT opponent with a .
        #the ARGUMENT for take_damage(damage) below is the damage VARIABLE of the bot attack (the bot in front of the period of the attack(opponent) FUNCTION)
        opponent.take_damage(self.attack_damage)
    
    #CLASS FUNCTION that handles taking damage
    #it takes damage as an ARGUMENT
    def take_damage(self, damage):
        #The health VARIABLE of the bot is subtracted by the different of the attcker's damage which is the ARGUMENT of the FUNCTION and attackee's defense
        #-= is the same as saying self.health = self.health - (damage - self.defense)
        self.health -= (damage - self.defense)
        #reduce the speed VARIABLE of the defending bot if it's health VARIABLE is less than 30
        if self.health < 30:
            self.speed -= 10

#NOTICE INDENT CHANGE

#create to VARIABLEs of TYPE BattleBot using the CONSTRUCTOR of CLASS BattleBot with custom ARGUMENTS
BattleBot1 = BattleBot(100, 30, 10, 60, "BOT1")
BattleBot2 = BattleBot(80, 60, 5, 70, "BOT2")

#create while loop that will loop until one of the two bot's health VARIABLE falls lower than 1
while (BattleBot1.health > 0 and BattleBot2.health > 0):
    #checks if bot1's speed VARIABLE is greate than bot2's speed VARIABLE
    if (BattleBot1.speed > BattleBot2.speed):
        #the attack(damage) FUNCTION with VARABLE BattleBot2 as the ARGUMENT is called on VARIABLE BattleBot1
        BattleBot1.attack(BattleBot2)
        #the attack(damage) FUNCTION with VARABLE BattleBot1 as the ARGUMENT is called on VARIABLE BattleBot2
        BattleBot2.attack(BattleBot1)
    elif (BattleBot2.speed > BattleBot1.speed):
        BattleBot2.attack(BattleBot1)
        BattleBot1.attack(BattleBot2)

#checks who won based off of who still has health above 0
if (BattleBot1.health <= 0):
    print(BattleBot2.name + " won!!!!")
else:
    print(BattleBot1.name + " won!!!!")