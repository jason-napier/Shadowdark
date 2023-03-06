import random
import os
import math


class Character:
    class Stat:
        def __init__(self):
            die_min = 1
            die_max = 6
            die_count = 3
            modifier_cutoff = 10
            modifier_divisor = 2
            self.value = sum([random.randint(die_min, die_max) for roll in range(die_count)])
            self.modifier = math.floor((self.value - modifier_cutoff) / modifier_divisor)

    _ancestries = {
        'Dwarf': 'Stout. Start with +2 HP (Included). Roll your hit point gains with advantage.',
        'Elf': 'Farsight. You get a +1 bonus to attack rolls with ranged weapons or a +1 bonus to spellcasting checks.',
        'Half-Orc': 'Mighty. You have a +1 bonus to attack and damage rolls with melee weapons.',
        'Halfling': 'Stealthy. Once per day, you can become invisible for 3 rounds.',
        'Goblin': 'Keen Senses. You cannot be surprised.',
        'Human': 'Ambitious. You gain one additional talent roll at 1st level.'
    }

    _background_list = ['Urchin', 'Wanted', 'Cult Initiate', "Thieves' Guild", 'Banished', 'Orphaned',
                        "Wizard's Apprentice", 'Jeweler', 'Herbalist', 'Barbarian', 'Mercenary', 'Sailor', 'Acolyte',
                        'Soldier', 'Ranger', 'Scout', 'Minstrel', 'Scholar', 'Noble', 'Chirurgeon']

    _stats = ['str', 'dex', 'con', 'int', 'wis', 'cha']

    _alignment_list = ['Lawful', 'Neutral', 'Chaotic']

    def __init__(self, character_name):
        min_hp = 1
        base_ac = 10
        hp_modifying_stat = 'CON'
        ac_modifying_stat = 'DEX'
        bonus_hp = {'dwarf': 2}
        gold_die_min = 1
        gold_die_max = 6
        gold_die_count = 2
        gold_modifier = 5

        self.name = character_name
        self.ancestry = random.choice(list(Character._ancestries.keys()))
        self.ancestry_talent = Character._ancestries[self.ancestry]
        self.alignment = random.choice(Character._alignment_list)
        self.background = random.choice(Character._background_list)
        self.stats = {}
        for stat in Character._stats:
            self.stats[stat.upper()] = Character.Stat()
        self.gold = sum([random.randint(gold_die_min, gold_die_max) for roll in range(gold_die_count)]) * gold_modifier
        self.hp = max(self.stats[hp_modifying_stat].modifier, min_hp)
        if self.ancestry.lower() in bonus_hp:
            self.hp += bonus_hp[self.ancestry.lower()]
        self.ac = base_ac + self.stats[ac_modifying_stat].modifier
        self.save_to_file()

    def save_to_file(self):
        try:
            dir_path = os.getcwd()
            filename = self.name + ".txt"
            full_path = os.path.join(dir_path, filename)
            with open(full_path, "w") as file:
                file.write("Name: " + self.name + "\n")
                file.write("Level: 0\n")
                file.write(f"Ancestry: {self.ancestry}" + "\n")
                file.write(f"Alignment: {self.alignment}" + "\n")
                file.write(f"Background: {self.background}" + "\n")
                file.write(f"HP: {self.hp}  AC: {self.ac}  \n")
                for stat_name, stat in self.stats.items():
                    file.write(
                        f'{stat_name}: {stat.value} ({"+" if stat.modifier > 0 else ""}{str(stat.modifier)})' + "\n")
                file.write(f"Ancestry Talent: {self.ancestry_talent}" + "\n")
                file.write(f"Gold: {self.gold}" + "\n")
            print("Character information saved to " + filename)
        except OSError as e:
            print(f"Something went wrong when trying to save {self.name} to file. Sorry it didn't work out")
            print(f"Error message:")
            print(e)


# Prompt the user for their character's name
name = input("What is your character's name? ")
char = Character(name)
