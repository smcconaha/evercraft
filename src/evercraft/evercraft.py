from evercraft.mod import modify

class Character():
    alignment = ['Good', 'Evil', 'Neutral']
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
        self.xp = 0
        self.level = 1
    def attack(self, roll, enemy):
        bonus = modify(self.skill["Strength"])
        roll = roll + bonus + (self.level - 1)
        if roll < enemy.armor:
            DP = 0
        elif roll >= enemy.armor:
            DP = 1 + bonus
            self.xp += 10
            self.level_up()
            if (roll - bonus) == 20:
                DP = DP * 2 
        enemy.damage(DP)
        return DP
    def damage(self, DP):
        self.HP = self.HP - DP
        if self.HP <= 0:
            self.isdead = True
    def armor_mod(self):
        armor_bonus = modify(self.skill["Dexterity"])
        self.armor += armor_bonus
    def hp_mod(self):
        if self.skill["Constitution"] >= 12:
            hp_bonus = modify(self.skill["Constitution"])
        else:
            hp_bonus = 0
        self.HP += hp_bonus
    def level_up(self):
        if self.xp == 1000:
            self.level += 1
            self.xp = 0
            if self.skill["Constitution"] >= 12:
                self.HP += (5 + modify(self.skill["Constitution"]))
            else:
                self.HP += 5
        

    # class Fighter(Character):
    #     def __init__ (self):#we only want to affect child NOT parent
    #         super().__init__()#need to also access the init method of parent, where super fn comes in