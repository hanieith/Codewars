import re

mytext = '23412hehllo, WORLD ,123DOTS ,shkutkoff@gmail.com, 123WORLD'

textlookfor = r"\D"

print(re.findall(textlookfor, mytext))