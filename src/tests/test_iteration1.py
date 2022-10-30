from evercraft.evercraft import * 
from evercraft.mod import *

def test_name():
    name = "Kateen"
    alignment = "Good"
    char = Character(name, alignment)
    assert not char.name == None

def test_alignment():
    alignment = 'Good'
    name = "Kateen"
    char = Character(name, alignment)
    assert not char.alignment == None

def test_armor():
    alignment = 'Good'
    name = "Kateen"
    char = Character(name, alignment)
    assert char.armor == 10

def test_HP():
    alignment = 'Good'
    name = "Kateen"
    char = Character(name, alignment)
    assert char.HP == 5

def test_attack_0dmg():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    damage = Kateen.attack(9, Cathaar) 
    assert damage == 0

def test_attack_1dmg():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    damage = Kateen.attack(11, Cathaar)
    assert damage == 1

def test_attack_2dmg():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    damage = Kateen.attack(20, Cathaar)
    assert damage == 2

def test_attack_armor_0dmg():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Cathaar.armor = 12
    damage = Kateen.attack(11, Cathaar)
    assert damage == 0 

def test_attack_armor_1dmg():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Cathaar.armor = 12
    damage = Kateen.attack(12, Cathaar)
    assert damage == 1 

def test_isdead():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good") 
    Cathaar.skill["Strength"] = 20
    Cathaar.attack(20, Kateen)
    assert Kateen.isdead == True

def test_damage0():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good") 
    Cathaar.attack(1, Kateen)
    assert Kateen.HP == 5

def test_damage1():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good") 
    Cathaar.attack(11, Kateen)
    assert Kateen.HP == 4

def test_damage2():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good") 
    Cathaar.attack(20, Kateen)
    assert Kateen.HP == 3

def test_HP0():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good") 
    Cathaar.attack(20, Kateen)
    Cathaar.attack(20, Kateen)
    Cathaar.attack(13, Kateen)
    assert Kateen.HP == 0


def test_dead():
    Kateen = Character("Kateen", "Good")
    Cathaar = Character("Cathaar", "Evil") 
    Cathaar.attack(20, Kateen)
    assert Kateen.isdead == False
    Cathaar.attack(20, Kateen)
    Cathaar.attack(13, Kateen)
    assert Kateen.isdead == True

def test_skill_change():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Kateen.setAbility("Kateen.skill.Strength", 12)
    assert Kateen.skill.Strength == 12


def test_skill():
    Kateen = Character("what", "Evil")
    assert not Kateen.skill == None 
    
def test_skill_exists():
    Kateen = Character("Kateen","Evil")
    assert not Kateen.skill["Strength"] == None

def test_skill_value():
    Kateen = Character("Kateen","Evil")
    assert Kateen.skill["Strength"] == 10

def test_all_skill_values():
    Kateen = Character("Kateen","Evil")
    Skills = ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"]
    test_pass = True
    for skill in Skills:
        if Kateen.skill[skill] != 10:
            test_pass = False
    assert test_pass

def test_skill_change():
   Kateen = Character("Kateen","Evil")
   Kateen.skill["Strength"] = 12
   assert Kateen.skill["Strength"] == 12

def test_mod_table():
    sum = modify(20)
    assert sum == 5

def test_mod_values():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Kateen.skill["Strength"] = 16
    Kateen.attack(17, Cathaar)
    assert Cathaar.HP == 1

def test_mod_value20():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Kateen.skill["Strength"] = 20
    Kateen.attack(20, Cathaar)
    assert Cathaar.HP == -7

def test_mod_value10():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Kateen.skill["Strength"] = 3
    Kateen.attack(10, Cathaar)
    assert Cathaar.HP == 5

def test_mod_value1():
    Kateen = Character("Kateen", "Evil")
    Cathaar = Character("Cathaar", "Good")
    Kateen.skill["Strength"] = 3
    Kateen.attack(10, Cathaar)
    assert Cathaar.HP == 5

def test_dexterity_mod():
    Cinder = Character("Cinder", "Evil")
    Cinder.skill["Dexterity"] = 12
    Cinder.armor_mod()
    assert Cinder.armor == 11

def test_constitution_mod():
    Glacius = Character("Glacius", "Good")
    Glacius.skill["Constitution"] = 14
    Glacius.hp_mod()
    assert Glacius.HP == 7

def test_can_gain_xp():
    Cinder = Character("Cinder", "Evil")
    Glacius = Character("Glacius", "Good")
    Cinder.attack(12, Glacius) #should clear armor
    assert Cinder.xp == 10

def test_can_level_xp_reset():
    Cinder = Character("Cinder", "Evil")
    Glacius = Character("Glacius", "Good")
    Cinder.xp = 990
    Cinder.attack(12, Glacius)
    assert Cinder.xp == 0

def test_can_level_up():
    Cinder = Character("Cinder", "Evil")
    Glacius = Character("Glacius", "Good")
    Cinder.xp = 990
    Cinder.attack(12, Glacius)
    assert Cinder.level == 2

def test_level_up_hp():
    Cinder = Character("Cinder", "Evil")
    Glacius = Character("Glacius", "Good")
    Cinder.xp = 990
    Cinder.attack(12, Glacius)
    assert Cinder.HP == 10

def test_level_up_hp_con():
    Cinder = Character("Cinder", "Evil")
    Glacius = Character("Glacius", "Good")
    Cinder.skill["Constitution"] = 12
    Cinder.xp = 990
    Cinder.attack(12, Glacius)
    assert Cinder.HP == 11

# def test_fighter_class():
#     Cathaar = Character("Cathaar", "Good")
#     Butterbean = Fighter("Butterbean", "Evil")
#     Butterbean.attack(10, Cathaar)
