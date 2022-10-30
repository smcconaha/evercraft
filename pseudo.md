# ITERATION 1
------------------------------------------------------------------------
I want to have a character with a unique name where we can set name

have a class of character with all of its unique traits

Name()

Alignment

Armor Class & Hit points

Character has hit points based on a roll (roll of 20 always hits || roll must meet or beat opponents armor class to hit)

Create two characters, one attacking character and one defense character

Attack method() 
    IF attacking character roll is less than defense character armor
        THEN no damage is done to defense character
    ELSE IF attacking character roll is equal to 20
        THEN defense character armor is reduced by two
    ELSE attacking character roll is greater than or equal to defense character armor and less than 20
        THEN defense character armor is reduced by one

Damage method() Input DP from attack() method  
    IF character HP is less than or equal to zero
        THEN character is dead (dead = true)

Character Health 
    IF attack is successful, (other character takes 1 point of damage when hit 
    IF a roll is a natural 20 then a critical hit is dealt and the damage is doubled
    WHILE hit points are 0 or fewer, the character is dead)


Character Ability Scores (Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma)
a list of variables and each variable will be set to a default of 10 that can be modifed in the class
once a new number is passed into it, 
loop through each variable and set it equal to an integer and then pass that into a function to determine the modifier

Exp points (When a successful attack occurs, the character gains 10 experience points)

Level Scaling (1000Xp = new level || hit points increase by 5 plus Con modifier || 1 is added to roll for every even level achieved (Ex: level 2 adds 1 to roll                                                                                                                                  if roll is 14 + 1)
------------------------------------------------------------------------

Evercraft Pseudo Revisit: Starting with Feature: Character Ability Modifiers Modify Attributes. Dexterity Modifier

Dexterity Modifier:
    Given dexterity value, search through modifier dictionary and return dexterity modifier
    Apply dexterity modifier to armor class

Constitution Modifier:
    IF constitution value is greater than or equal to 12
    THEN search through modifier dictionary and return dexterity modifier
    AND Apply constitution modifier to hitpoints
