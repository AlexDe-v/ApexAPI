import apex

apex.token = "TOKEN"

name = "Shroud"

user = apex.get_user(name, "PC") # Switch isn't supported!

lvl = user['global']['level']
rank = user['global']['rank']['rankName']

print(f'{name} is level {lvl} and is {rank}.')