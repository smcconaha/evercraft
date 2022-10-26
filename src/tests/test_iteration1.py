from evercraft.evercraft import * 

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


# def test_separate_chars():
#     Kateen = Character("Kateen", "Evil", 18)
#     Cathaar = Character("Cathaar", "Good", 12)

#     assert Kateen.roll == 18


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


# def test_isdead():
#     Kateen = Character("Kateen", "Evil")
#     assert Kateen.isdead == False
#     isdead = Kateen.damage()
#     assert Kateen.isdead == True


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



