#Name: Carl Lewis (Luke Brooks, Tatianna Stryjewski, and Matthew Martin)
#email: stryjete@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description:  Invoking functions and decypting 
#Citations: 
#Anything else that's relevant: 
#main.py

import json
from functionsPackage.functions import *
from PIL import Image, ImageFilter, ImageDraw,ImageFont

json_file = 'hints.json'
english_file = 'english.txt'
team = 'Carl Lewis'

decrypted_location = decrypt_location(json_file, english_file, team)
print(decrypted_location)

im = Image.open("..\imagePackage\CarlLewisPhoto.jpeg")
my_image = load_image("..\imagePackage\CarlLewisPhoto.jpeg")
try:
    my_image.show(my_image)
except Exception as e:
    print(e)
    pass
