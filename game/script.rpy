# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define template_person = Character("A")

init -20 python:
    import os
    import yaml
    import json
    from renpy.character import ADVCharacter
    
    def read_all_bgs():
        renpy_files = renpy.list_files()
        renpy_files = [x.split('/') for x in renpy_files]
        bg_files = [x for x in renpy_files if x[0] == 'images' and x[1] == 'bgs']

        bg_name_list = []
        for bg_path_split in bg_files:
            bg_path = "/".join(bg_path_split[1:])

            bg_name = 'bg ' + ' '.join(['_'.join(x.split()).replace('-','_').lower() for x in bg_path_split[2:]]).split('.')[0]
            bg_name_list += [bg_name]

            bg_image = Image(bg_path, zoom=2)
            bg_image = Transform(bg_image, ysize=1080, xsize=1920)
            renpy.image(bg_name, bg_image)
        return bg_name_list

    def read_all_character_images():
        renpy_files = renpy.list_files()
        renpy_files = [x.split('/') for x in renpy_files]
        character_files = [x for x in renpy_files if x[0] == 'images' and x[1] == 'characters']
        character_list = list(set([x[-3] for x in character_files if x[-1].split('.')[-1].lower() in ['png','webp']]))

        character_filepaths_dict = {}
        character_desc_all = {}
        exp_name_all = {}
        exp_name_all_per_expression = {}
        character_speaker_list = []
        for character in character_list:
            character_desc_files = [x for x in character_files if x[2] == character and x[-1].split('.')[-1].lower() in ['yaml','yml','json']]
            
            character_desc_dict = {
                'name': character,
                'direction': 'left',
                'scaling': 1,
                'fullsize': False,
                'color': '#FFFFFF'
            }

            if character_desc_files:
                character_desc_file = character_desc_files[0]

                if character_desc_file[-1].split('.')[-1].lower() in ['yaml','yml']:
                    character_desc_file = "/".join(character_desc_file)
                    with renpy.open_file(character_desc_file) as character_desc_file_open:
                        character_desc_dict_temp = yaml.safe_load(character_desc_file_open)
                        for k,v in character_desc_dict_temp.items():
                            character_desc_dict[k] = v
                elif character_desc_file[-1].split('.')[-1].lower() in ['json']:
                    character_desc_file = "/".join(character_desc_file)
                    with renpy.open_file(character_desc_file) as character_desc_file_open:
                        character_desc_dict = json.load(character_desc_file_open)
                        for k,v in character_desc_dict_temp.items():
                            character_desc_dict[k] = v
                            
                character_speaker_list += ['{code} = Character("{name}", kind=store.adv, color="{color}")'
                                .format(
                                    code = character,
                                    name = character_desc_dict['name'],
                                    color = character_desc_dict['color']
                                )]
                
            character_desc_all[character] = character_desc_dict

            character_expressions = [x for x in character_files if x[2] == character and x[-1].split('.')[-1].lower() in ['png','webp']]

            character_filepaths_dict[character] = ['/'.join(path_lst) for path_lst in character_expressions]
            
            exp_name_list_temp = []
            exp_name_list_temp_per_expression = {}
            for exp_path_split in character_expressions:
                exp_path = "/".join(exp_path_split[1:])

                exp_name = ' '.join(exp_path_split[2:]).split('.')[0]
                exp_name_list_temp += [exp_name]

                expression_name = exp_name.split(' ')[-1]
                if expression_name in exp_name_list_temp_per_expression:
                    exp_name_list_temp_per_expression[expression_name] += [exp_name]
                else: 
                    exp_name_list_temp_per_expression[expression_name] = [exp_name]

                exp_image = Image(exp_path, zoom=character_desc_dict['scaling'])

                if character_desc_dict['direction'] == 'right':
                    exp_image = Transform(exp_image, zoom=character_desc_dict['scaling'], xzoom=-1)
                else:
                    exp_image = Transform(exp_image, zoom=character_desc_dict['scaling'])


                renpy.image(exp_name, exp_image)

            exp_name_all[character] = exp_name_list_temp
            exp_name_all_per_expression[character] = exp_name_list_temp_per_expression

        return exp_name_all, exp_name_all_per_expression, character_speaker_list, character_filepaths_dict, character_desc_all

    def make_composites(exp_dict):
        list_cond = []
        for char_name, char_exp_list in exp_dict.items():
            cond_switch = "image " + char_name + ' = ConditionSwitch(\n'
            
            for exp in char_exp_list: 
                exp_attr = exp.split(' ')
                # txt_temp = '"' + char_name + ".outfit == '" + exp_attr[1] + "' and " + char_name +".expression == '" + exp_attr[-1] + "',"  + exp + "',\n"
                txt_temp = '"' + char_name + ".outfit == '" + exp_attr[1] + \
                        "' and " + char_name +".expression == '" + exp_attr[-1] + \
                        "'\",\""  + exp + "\",\n"
                
                cond_switch += txt_temp
            
            cond_switch += ")"
            list_cond += [cond_switch]

            # renpy.game.script.load_appropriate_file(".rpyc", ".rpy", work_dir, filename, [])

        return list_cond

    def make_composites_per_expression(exp_dict):
        list_cond = []
        for char_name, char_expression_dict in exp_dict.items():
            for expression_name, sprite_list in char_expression_dict.items():
                cond_switch = "image " + char_name + ' ' + expression_name + ' = ConditionSwitch(\n'
                
                for exp in sprite_list: 
                    exp_attr = exp.split(' ')

                    txt_temp = '"' + char_name + ".outfit == '" + exp_attr[1] + "'\",\""  + exp + "\",\n"
                    
                    cond_switch += txt_temp
                
                cond_switch += ")"
                list_cond += [cond_switch]

            # renpy.game.script.load_appropriate_file(".rpyc", ".rpy", work_dir, filename, [])

        return list_cond

    def set_default_outfit_exp(exp_dict):
        for char_name, char_exp_list in exp_dict.items(): 
            exp = char_exp_list[0]
            exp_attr = exp.split(' ')

            renpy.load_string('$ '+  char_name + ".outfit = '"+ exp_attr[1] + "'")
            renpy.load_string('$ '+  char_name + ".expression = '"+ exp_attr[-1] + "'")

        

    character_exp_dict, character_exp_dict_per_expression,  character_speaker_list, character_filepaths_dict, character_desc = read_all_character_images()
    bg_list = read_all_bgs()

    list_cond = make_composites(character_exp_dict)

    list_cond_exp = make_composites_per_expression(character_exp_dict_per_expression)

    for speaker_x in character_speaker_list:
        exec(speaker_x)

    for cond in list_cond:
        renpy.load_string(cond)

        
    for cond in list_cond_exp:
        renpy.load_string(cond)

    set_default_outfit_exp(character_exp_dict)




transform faceright:
    xzoom -1.0

transform faceleft:
    xzoom 1.0


label start:
    python:

        # for char_name, char_exp_list in character_exp_dict.items(): 
        #     exp = char_exp_list[0]
        #     exp_attr = exp.split(' ')

        #     exec(char_name + ".outfit = '"+ exp_attr[1] + "'")
        #     exec(char_name + ".expression = '"+ exp_attr[-1] + "'")
        # # TODO: Default Values for outfit and expression

        exec("morgan_lily.outfit = 'asc2'")
        morgan_lily.expression = 'm0_b0_l0_r0'
        
        davinci.outfit = 'npc'
        davinci.expression = '0'

        artoria.outfit = 'asc1'
        artoria.expression = '0'

    # The game starts here.
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    call bermuda_lb

    # This ends the game.

    return
