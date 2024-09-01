
init:
    python:
        def get_sorted(lx):
            try:
                return sorted(lx, key= lambda x: int(x))
            except:
                return sorted(lx)

default selectedCharacter = "mash"

screen CharacterListUI():
    tag menu
    
    add gui.my_room_background xsize 1920 ysize 1080 xalign 0.5 yalign 0.5

    default outfitMenuShow = False
    hbox:
        frame:
            # background Solid("#0000FF7F")
            ysize 1080
            xsize 480

            vbox:
                xalign 0.5
                yalign 0.5

                text "Character List"
                null height 30

                frame:
                    side ("c r"):
                        area (1,0,280,800)
                        viewport id "character_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                            draggable True mousewheel True
                            vbox:
                                for character_code in sorted(character_exp_dict):
                                    textbutton _(character_code):
                                        action SetVariable("selectedCharacter", character_code), ShowMenu("CharacterDetailsUI")
                                        tooltip character_code
                        vbar value YScrollValue("character_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG
                null height 20 #just a height set.

                textbutton "Return" : 
                    action Return()

                

                # textbutton _("ereshkigal"):
                #     action SetScreenVariable("selectedCharacter", "ereshkigal")
                #     tooltip "ereshkigal"
                # textbutton _("morgan_lily"):
                #     action SetScreenVariable("selectedCharacter", "morgan_lily")
                #     tooltip "morgan_lily"
                # textbutton _("davinci"):
                #     action SetScreenVariable("selectedCharacter", "davinci")
                #     tooltip "davinci"
                # textbutton _("altera_sefar"):
                #     action SetScreenVariable("selectedCharacter", "altera_sefar")
                #     tooltip "altera_sefar"
                    
        if GetTooltip():
            $ selectedCharacter = GetTooltip()
        hbox:
            ysize 1080
            xsize 1080
            $ temp_lst = character_exp_dict[selectedCharacter]
            $ temp_desc = character_desc[selectedCharacter]
            # text "[temp_lst]"

            $ tempt = temp_lst[0]
            $ temp_scale = temp_desc['scaling']
            # text "[tempt]"

            add tempt at left
            # if selectedCharacter == 'morgan_lily':
            #     add tempt yoffset -200 at center 
            # else:
            #     add tempt at center
            # add "morgan_lily asc3_w1 m0_b0_l0_r0" ypos -200

screen CharacterDetailsUI():
    tag menu
    
    add gui.my_room_background xsize 1920 ysize 1080 xalign 0.5 yalign 0.5

    default selectedOutfit = character_exp_dict[selectedCharacter][0].split()[1]
    default selectedExpression = character_exp_dict[selectedCharacter][0].split()[-1]
    hbox:
        frame:
            ysize 1080
            xsize 480

            vbox:
                xalign 0.5
                yalign 0.5

                text "Outfit List"
                null height 20

                $ character_outfits = [x.split()[1] for x in character_exp_dict[selectedCharacter]]
                $ character_outfits = list(set(character_outfits))
                $ sorted_character_outfits = get_sorted(character_outfits)

                frame:
                    side ("c r"):
                        area (1,0,280,250)
                        viewport id "outfit_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                            draggable True mousewheel True
                            vbox:
                                for outfit_code in sorted_character_outfits:
                                    textbutton _(outfit_code):
                                        action SetScreenVariable("selectedOutfit", outfit_code)
                                        tooltip outfit_code
                        vbar value YScrollValue("outfit_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG
                null height 20 #just a height set.


                $ character_expressions = [x.split()[2] for x in character_exp_dict[selectedCharacter]]
                $ character_expressions = list(set(character_expressions))
                $ sorted_character_expressions = get_sorted(character_expressions)


                text "Expression List"
                null height 20
                frame:
                    side ("c r"):
                        area (1,0,280,450)
                        viewport id "exp_scroller": #REMEMBER YOUR VIEWPORT ID SO THE SCROLLBAR IS PLACED FOR IT
                            draggable True mousewheel True
                            vbox:
                                for exp_code in sorted_character_expressions:
                                    textbutton _(exp_code):
                                        action SetScreenVariable("selectedExpression", exp_code)
                                        tooltip exp_code
                        vbar value YScrollValue("exp_scroller") #TAKES YOUR VIEWPORT ID AS THE ARG
                null height 20 #just a height set.

                textbutton "Return" action ShowMenu("CharacterListUI")

                    
        # if GetTooltip():
        #     $ selectedOutfit = GetTooltip()

        hbox:
            ysize 1080
            xsize 1080
            $ tempt = selectedCharacter + " " + selectedOutfit + " " + selectedExpression
            if tempt in character_exp_dict[selectedCharacter]:  
                $ char_img = tempt
            add char_img at left