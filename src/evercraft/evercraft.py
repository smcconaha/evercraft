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
#       a list of variables and each variable will be set to a default of 10 that can be modifed in the class
#       once a new number is passed into it, 
#       loop through each variable and set it equal to an integer and then pass that into a function to determine the modifier
#       
#


#   Exp points (When a successful attack occurs, the character gains 10 experience points)
#             
#
#
#


#   Level Scaling (1000Xp = new level || hit points increase by 5 plus Con modifier || 1 is added to roll for every even level achieved (Ex: level 2 adds 1 to roll
#                                                                                                                                          if roll is 14 + 1)
#------------------------------------------------------------------------

# class setAbility():
    # def __init__(self, Type, Num):
    #     for Ability in Character.Skills:
    #         if Ability == Type:
    #             Abilities(Type, Num)
                

# class Abilities():
#     def __init__(self, Type, Num):
#         self.Type = Num

# class Abilities():
    # def __init__(self):
    #     self.Strength = 10
    #     self.Dexterity = 10
    #     self.Constitution = 10
    #     self.Wisdom = 10
    #     self.Intelligence = 10
    #     self.Charisma = 10
from evercraft.mod import modify

class Character():
    def __init__(self, name, alignment):
        self.skill =  {
            "Strength" : 10,
            "Dexterity" : 10,
            "Constitution" : 10,
            "Wisdom" : 10,
            "Intelligence" : 10, 
            "Charisma" : 10
        }      
        self.name = name
        self.alignment = alignment
        self.HP = 5 
        self.isdead = False
        self.armor = 10
        self.xp = 1000
    def attack(self, roll, enemy):
        bonus = modify(self.skill["Strength"])
        roll = roll + bonus
        if roll < enemy.armor:
            DP = 0
        if roll >= enemy.armor:
            DP = 1 + bonus
        if (roll - bonus) == 20:
            DP = DP * 2 
        enemy.damage(DP)
        return DP
    def damage(self, DP):
        self.HP = self.HP - DP
        if self.HP <= 0:
            self.isdead = True

    # class Fighter(Character):
    #     def __init__ (self):#we only want to affect child NOT parent
    #         super().__init__()#need to also access the init method of parent, where super fn comes in