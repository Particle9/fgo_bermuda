init python:
    g= Gallery()

    g.button("my room")
    g.image("bg my_room wandering_sea")
    
    g.button("my room 2")
    g.image("bg my_room storm_border")
    
    g.button("my room 3")
    g.image("bg my_room shadow_border")
    
    g.transition = dissolve


screen gallery:
    tag menu
    text "Backgrounds"

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        add g.make_button(name="my room", unlocked='thumbnails/bgs/my_room/wandering_sea.webp')
        add g.make_button(name="my room 2", unlocked='thumbnails/bgs/my_room/storm_border.webp')
        add g.make_button(name="my room 3", unlocked='thumbnails/bgs/my_room/shadow_border.webp')

        textbutton "Return" action Return()