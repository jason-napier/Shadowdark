import random
import os

#Chose Background
background_list = ['Urchin', 'Wanted', 'Cult Initiate', "Thieves' Guild", 'Banished', 'Orphaned', "Wizard's Apprentice", 'Jeweler', 'Herbalist', 'Barbarian', 'Mercenary', 'Sailor', 'Acolyte', 'Soldier', 'Ranger', 'Scout', 'Minstrel', 'Scholar', 'Noble', 'Chirurgeon']

Background = random.choice(background_list)

#Roll Stats
STR = sum([random.randint(1,6) for i in range(3)])
DEX = sum([random.randint(1,6) for i in range(3)])
CON = sum([random.randint(1,6) for i in range(3)])
INT = sum([random.randint(1,6) for i in range(3)])
WIS = sum([random.randint(1,6) for i in range(3)])
CHA = sum([random.randint(1,6) for i in range(3)])

#Get Modifiers
STR_Mod = -4 if STR <= 3 else -3 if STR <= 5 else -2 if STR <= 7 else -1 if STR <= 9 else 0 if STR <= 11 else 1 if STR <= 13 else 2 if STR <= 15 else 3 if STR <= 17 else 4
DEX_Mod = -4 if DEX <= 3 else -3 if DEX <= 5 else -2 if DEX <= 7 else -1 if DEX <= 9 else 0 if DEX <= 11 else 1 if DEX <= 13 else 2 if DEX <= 15 else 3 if DEX <= 17 else 4
CON_Mod = -4 if CON <= 3 else -3 if CON <= 5 else -2 if CON <= 7 else -1 if CON <= 9 else 0 if CON <= 11 else 1 if CON <= 13 else 2 if CON <= 15 else 3 if CON <= 17 else 4
INT_Mod = -4 if INT <= 3 else -3 if INT <= 5 else -2 if INT <= 7 else -1 if INT <= 9 else 0 if INT <= 11 else 1 if INT <= 13 else 2 if INT <= 15 else 3 if INT <= 17 else 4
WIS_Mod = -4 if WIS <= 3 else -3 if WIS <= 5 else -2 if WIS <= 7 else -1 if WIS <= 9 else 0 if WIS <= 11 else 1 if WIS <= 13 else 2 if WIS <= 15 else 3 if WIS <= 17 else 4
CHA_Mod = -4 if CHA <= 3 else -3 if CHA <= 5 else -2 if CHA <= 7 else -1 if CHA <= 9 else 0 if CHA <= 11 else 1 if CHA <= 13 else 2 if CHA <= 15 else 3 if CHA <= 17 else 4

#Get Ancestry
ancestry_list = ['Dwarf', 'Elf', 'Half-Orc', 'Halfling', 'Human', 'Goblin']
Ancestry = random.choice(ancestry_list)

#Get Ancestry Talent
Ancestry_Talent = ''
if Ancestry == 'Dwarf':
    Ancestry_Talent = 'Stout. Start with +2 HP (Included). Roll your hit point gains with advantage.'

elif Ancestry == 'Elf': 
    Ancestry_Talent = 'Farsight. You get a +1 bonus to attack rolls with ranged weapons or a +1 bonus to spellcasting checks.'
    
elif Ancestry == 'Half-Orc':
    Ancestry_Talent = 'Mighty. You have a +1 bonus to attack and damage rolls with melee weapons.'
    
elif Ancestry == 'Halfling': 
    Ancestry_Talent = 'Stealthy. Once per day, you can become invisible for 3 rounds.'
    
elif Ancestry =='Goblin':
    Ancestry_Talent = 'Keen Senses. You cannot be surprised.'

elif Ancestry == 'Human':
    Ancestry_Talent = 'Ambitious. You gain one additional talent roll at 1st level.'

else:
    print("Error!")


#Get HP
if CON_Mod >0:
    HP = CON_Mod
else:
    HP = 1

if Ancestry == "Dwarf":
    HP += 2

#Get Alignment
alignment_list = ['Lawful', 'Neutral', 'Chaotic']
Alignment = random.choice(alignment_list)

#Get Gold/Gear
Gold = sum([random.randint(1,6) for i in range(3)])*5
   
# Prompt the user for their character's name
name = input("What is your character's name? ")

#Create Fiel

# Get current working directory
dir_path = os.getcwd()

# Create a text file with the character's name
filename = name + ".txt"

# Join the directory and filename using os.path.join()
full_path = os.path.join(dir_path, filename)

#Open the file for writing and write the variable values
with open(full_path, "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Level: 0\n")
    file.write("Ancestry: " + Ancestry + "\n")
    file.write("Alignment: " + Alignment + "\n")
    file.write("Background: " + Background + "\n")
    file.write("HP: " + str(HP) + ", AC:   \n")
    file.write("STR: " + str(STR) + "(" + str(STR_Mod) +")" "\n")
    file.write("DEX: " + str(DEX) + "(" + str(DEX_Mod) +")" "\n")
    file.write("CON: " + str(CON) + "(" + str(CON_Mod) +")" "\n")
    file.write("INT: " + str(INT) + "(" + str(INT_Mod) +")" "\n")
    file.write("WIS: " + str(WIS) + "(" + str(WIS_Mod) +")" "\n")
    file.write("CHA: " + str(CHA) + "(" + str(CHA_Mod) +")" "\n")
    file.write("Ancestry Talent: " + str(Ancestry_Talent) + "\n")
    file.write("Gold: " + str(Gold) + "\n")

#Confirmation message
print("Character information saved to " + filename)
