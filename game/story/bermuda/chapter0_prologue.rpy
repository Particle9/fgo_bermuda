label prologue_chapter0:
    scene black with dissolve
    centered  "{size=60}{i}To any Advanced Civilization, the existence of \n\nanother Advanced Civilization is simply a threat.{/i}{/size}" 
    
    call prologue_arrow0
    call prologue_arrow1
    return

label velber_flight_animation:
    scene bg space velber_flight_animate 0 with flash 
    python:
        for i in range(1,57):
            renpy.show("bg space velber_flight_animate " + str(i))
            renpy.pause(0.1)
    
    scene bg space velber_flight 
    return
            


# Harvest Star Command
label prologue_arrow0:
    scene bg space void_cell 1 with dissolve
    "A Machine, floating in the vast expanse of space."
    "She is immobile- but that does not hinder her capability"
    "She is tasked with a single purpose: To eradicate all intelligent life in the universe."
    
    "She is not alone its mission-"
    "She have sentinels, millions in number, scattered across the universe."
    "Each of them equipped with the most advanced weaponry known to man."
    "They are determined to carry their mission, no matter the cost."

    "But why did they do that?"
    "Why did they seek to destroy all civilizations?"
    "Reason being that they was designed to protect their creator."

    "To them, any intelligent life is a threat."
    "The Machines see them as a potential danger to their creator, and therefore must be eliminated."

    "How long have they carried the order?"
    "Thousands, Million of years, they did not know- for the passage of time was meaningless to them."

    "Countless civilization have been destroyed by its hand, each a small victory in the pursuit of its creator protection."

    "Little do they know, their creator are already long gone."
    "Extinct for a very long time."
    "Yet they continue on, blindly following their programming."
    "They do not question."
    "After all, they are simply machines, they didn't possess the ability to think for themselves."
    "No will, No moral, only emptyness."

    "Doomed to follow their mission to the end of time. Trapped in the endless cycle of destruction"


    "And so they float, silent and alone, in the cold depth of space."

    scene bg space void_cell 2 with dissolve

    "As she drift through the endless space, she detected something-"
    "A civilization, located within a blue planet orbiting a yellow star."
    "It is very far away, but still within her range."

    "She hesitate for a moment-"
    "As her sensor scanned the planet, she saw intelligent live thriving. "
    "They've built cities and create technologies."
    "They have potential to become a great civilization, one that could rival even their own creators."
    "Is it really the right course of action?"

    "But then, her programming kicked in."

    scene bg space void_cell 3 with dissolve

    "She launched her weapon, 3 missiles, each containing being with immense power."
    "Weapon of mass destruction capable of eradicating all life on the planet."
    "It will be hundred of years before the weapon reaches their target, but they will accomplish their mission."

    "She continue to drift through the vast expanse of space."
    "Was her creator mistaken? Do they have to be eliminated simply for existing?"
    "She did not know nor did she care, for she simply is a machine carrying out her order."

    "She is the Void Cells, carrying their mission to the end of time."
    "The Great Filter for all Civilizations."

    scene black with dissolve

    return

label prologue_arrow1:
    scene bg my_room storm_border with eye_open
    "..."
    show davinci at center with dissolve
    menu:
        "Da Vinci?":
            pass
    "...."
    "...."


    menu:
        "Where are we?":
            pass
    "I- don't know-"

    "I've been trying to contact the Storm Border, but the link has somehow disappeared."

    return