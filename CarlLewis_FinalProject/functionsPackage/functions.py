#Name: Carl Lewis (Luke Brooks, Tatianna Stryjewski, and Matthew Martin)
#email: stryjete@mail.uc.edu
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Invoking functions and decypting 
#Citations: 
#Anything else that's relevant: 
#functions.py

from PIL import Image, ImageFilter, ImageDraw,ImageFont
import json
from numpy.distutils.fcompiler import none

def decrypt_location(json_file, english_file, team):
    
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(english_file, 'r') as f:
        english = f.read().splitlines()

    decrypted = ''
    for index in data[team]:
        decrypted += english[int(index) -1 ] + ' '
        
    return decrypted.strip()

def load_image(filename):
    try:
        myimage = Image.open(filename)
        myimage.load()
    except:
        raise Exception("Unable to load" + filename)
        return none
    return myimage


