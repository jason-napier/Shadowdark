import random
import math

#Chose Background
Background = random.choice(['Urchin', 'Wanted', 'Cult Initiate', "Thieves' Guild", 'Banished', 'Orphaned', "Wizard's Apprentice", 'Jeweler', 'Herbalist', 'Barbarian', 'Mercenary', 'Sailor', 'Acolyte', 'Soldier', 'Ranger', 'Scout', 'Minstrel', 'Scholar', 'Noble', 'Chirurgeon'])

def roll_stat_or_gold(is_gold = False):
    if is_gold == True:
        gold_multiplier = 5
    else:
        gold_multiplier = 1
    return sum([random.randint(1,6) for i in range(3)]) * gold_multiplier

def get_stat_mod(stat):
    return math.floor((stat-10)/2)


#Roll Stats
STR = roll_stat_or_gold()
DEX = roll_stat_or_gold()
CON = roll_stat_or_gold()
INT = roll_stat_or_gold()
WIS = roll_stat_or_gold()
CHA = roll_stat_or_gold()

Ancestry = random.choice([
    {'name': 'Dwarf', 'talent': 'Stout. Start with +2 HP (Included). Roll your hit point gains with advantage.'},
    {'name': 'Elf', 'talent': 'Farsight. You get a +1 bonus to attack rolls with ranged weapons or a +1 bonus to spellcasting checks.'},
    {'name': 'Half-Orc', 'talent': 'Mighty. You have a +1 bonus to attack and damage rolls with melee weapons.'},
    {'name': 'Halfling', 'talent': 'Stealthy. Once per day, you can become invisible for 3 rounds.'},
    {'name': 'Goblin', 'talent': 'Keen Senses. You cannot be surprised.'},
    {'name': 'Human', 'talent': 'Ambitious. You gain one additional talent roll at 1st level.'}
])

#Get HP
if get_stat_mod(CON) > 0:
    HP = get_stat_mod(CON)
else:
    HP = 1

if Ancestry["name"] == "Dwarf":
    HP += 2

#Get Alignment
Alignment = random.choice(['Lawful', 'Neutral', 'Chaotic'])

#Get Gold/Gear
Gold = roll_stat_or_gold(True)

# Prompt the user for their character's name
name = input("What is your character's name? ")

#Create Field

#Open the file for writing and write the variable values
with open(f"{name}.txt", "w") as file:
    file.seek
    file.write("Name: " + name + "\n")
    file.write("Level: 0\n")
    file.write("Ancestry: " + Ancestry["name"] + "\n")
    file.write("Alignment: " + Alignment + "\n")
    file.write("Background: " + Background + "\n")
    file.write("HP: " + str(HP) + ", AC:   \n")
    file.write("STR: " + str(STR) + "(" + str(get_stat_mod(STR)) +")" "\n")
    file.write("DEX: " + str(DEX) + "(" + str(get_stat_mod(DEX)) +")" "\n")
    file.write("CON: " + str(CON) + "(" + str(get_stat_mod(CON)) +")" "\n")
    file.write("INT: " + str(INT) + "(" + str(get_stat_mod(INT)) +")" "\n")
    file.write("WIS: " + str(WIS) + "(" + str(get_stat_mod(WIS)) +")" "\n")
    file.write("CHA: " + str(CHA) + "(" + str(get_stat_mod(CHA)) +")" "\n")
    file.write("Ancestry Talent: " + str(Ancestry["talent"]) + "\n")
    file.write("Gold: " + str(Gold) + "\n")

#Confirmation message
print(f"Character information saved to {name}.txt")
