# ITERATION 1

#------------------------------------------------------------------------
#   I want to have a character with a unique name where we can set name


#   have a class of character with all of its unique traits


#   Name()


#   Alignment


#   Armor Class & Hit points


#   Character has hit points based on a roll (roll of 20 always hits || roll must meet or beat opponents armor class to hit)
#           Create two characters, one attacking character and one defense character
#           Attack method() If attacking character roll is less than defense character armor
#                               Then no damage is done to defense character
#                           Else if attacking character roll is equal to 20
#                               Then defense character armor is reduced by two
#                           Else attacking character roll is greater than or equal to defense character armor and less than 20
#                               Then defense character armor is reduced by one
#           Damage method() Input DP from attack() method
#                           
#                           If character HP is less than or equal to zero
#                           Then character is dead (dead = true)

#   Character Health If attack is successful, (other character takes 1 point of damage when hit 
#           If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
#           when hit points are 0 or fewer, the character is dead)


#   Character Ability Scores (Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma)


#   Exp points (When a successful attack occurs, the character gains 10 experience points)


#   Level Scaling (1000Xp = new level || hit points increase by 5 plus Con modifier || 1 is added to roll for every even level achieved (Ex: level 2 adds 1 to roll
#                                                                                                                                          if roll is 14 + 1)
#------------------------------------------------------------------------


class Character():
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.armor = 10
        self.HP = 5 
        self.isdead = False
    def attack(self, roll, enemy):
        DP = 1
        if roll < enemy.armor:
            DP = 0
        if roll >= enemy.armor:
            DP = 1
        if roll == 20:
            DP = DP * 2
        enemy.damage(DP)
        return DP
    def damage(self, DP):
        self.HP = self.HP - DP

