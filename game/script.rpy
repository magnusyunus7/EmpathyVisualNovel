# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Fred")
define g = Character("Gary")
define n = Character("Narrator")
image bg_cafeteria = im.Scale("images/bg_cafeteria.png", 1920, 1080)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_cafeteria with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    n "It's a Thursday evening at the SUTD canteen."
    n "The dinner rush has long thinned out, most people have retreated to their rooms, their deadlines, their screens."
    n "The overhead lights cast everything in a warm, slightly tired glow."
    n "Somewhere nearby, a ceiling fan hums at a speed that doesn't quite cool anything."
    
    show gary_neutral at left with moveinleft

    n "You are Gary. Term 5 EPD student."
    n "You've been meaning to catch up with Fred for weeks, tonight was the first window either of you could find."
    n "You grab your mixed rice, half a sugarcane juice and spot Fred already at the corner table."
    n "You weave past a few lingering students and slide into the seat across from him."

    show fred_distant at right with moveinright
    hide gary_neutral with dissolve

    n "He doesn't look up when you sit down."
    n "You arrange your tray. Unwrap your cutlery. Take a slow sip of your drink. Still nothing from him."
    n "You've known Fred since Term 1."
    n "You've pulled all-nighters together, complained about the same professors, split delivery fees more times than you can count."
    n "This quietness is not like him at all."

    show gary_neutral at left with moveinleft

    g "Hey. Didn't see you in the library today."

    hide fred_distant
    show fred_faintsmile at right

    f "Yeah... sorry. I've just been... I don't know. Out of it lately."
    n "He looks back down at his plate. The food is barely touched."
    n "You watch him push a piece of tofu to the side and leave it there."

    
    # This ends the game.

    return
