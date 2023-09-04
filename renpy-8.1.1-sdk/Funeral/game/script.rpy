# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narrator")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg prolog_1
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    e "..."

    e "..."
    
    scene bg prolog_2
    with fade
   
    e "..."

    e "..."
    
    scene bg prolog_3
    with fade
    
    e "..."

    e "..."

    scene bg prolog_4
    with fade
   
    e "..."

    e "..."
    
    scene bg prolog_5
    with fade
    
    e "..."

    e "..."
    
    scene bg prolog_7
    with fade
    
    e "..."

    e "..."
    # This ends the game.

    return
