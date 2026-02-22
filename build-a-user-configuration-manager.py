** start of main.py **

#User Configuration Manager

test_settings={'Action':'nodef','broz':'tris','crr':'jros'}

def add_setting(setting_dict,item):
    key, value = item
    key=key.lower()
    #print(key)
    if key.lower() in setting_dict.keys(): return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        setting_dict[key]=value.lower()
        return f"Setting '{key}' added with value '{value.lower()}' successfully!"

#print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
#print(test_settings)

def update_setting(setting_dict, item):
    key,value=item
    if key.lower() in setting_dict.keys():
        setting_dict[key.lower()]=value.lower()
        return f"Setting '{key}' updated to '{value.lower()}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting_dict, key):
    key=key.lower()
    if key in setting_dict.keys():
        del setting_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(setting_dict):
    if len(setting_dict)==0:
        #print("No setting available")
        return "No settings available."
    else:
        view_string= ("Current User Settings:""\n")
        for key, value in setting_dict.items():
            setting = f"{key.capitalize()}: {value}"+"\n"
            view_string += setting
        return view_string


#print(view_settings(test_settings))


** end of main.py **

