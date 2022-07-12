from datetime import datetime
import random
import json
import textwrap
# from tinydb import TinyDB, Query
from PIL import Image, ImageFont, ImageDraw

rmLi = ["Breeze.png", "Cloud.png", "Rainy Day.png", "Sandstorm.png", "Soft Pink.png"]
rImg = "../BGs/" + random.choice(rmLi)
# q = Query()
# tododb = TinyDB("To Do DB.json")
# donedb = TinyDB("Done DB.json")
# co = len(tododb.all())
# openDDfile = open("Done DB.json", "r")
# DDfile = json.load(openDDfile)
# DDfileValues = DDfile.values()
# openTDDfile = open("To Do DB.json")
# TDDfile = json.load(openTDDfile)
# TDDfileValues = TDDfile.values()
# TDDfileValuesLength = (len(TDDfileValues) + 1)
# DDfileValuesLength = (len(DDfileValues) + 1)
# for i in DDfileValues:
#     DDValue = i["Book"]
# for i in TDDfileValues:
#     TDDValue = i["Book"]
#     TDDVerse = i["Verse"]
#     # for n in range(TDDfileValuesLength):
#     if TDDValue in DDValue:
#         print("Already Done!")
#         # for i in DDfileValues:
#             # DDValue = i["Book"]
#     elif TDDValue not in DDValue:
print("Creating...")
W, H = (2000, 2000)
img = Image.open(rImg)
txtFont = ImageFont.truetype("../Font/PlayfairDisplay-Medium.ttf", 115)
verse = input(">>>")
para = textwrap.wrap(verse, width = 30)
edit = ImageDraw.Draw(img)
w, h = edit.textsize(verse)
edit.text((W/2, H/2), verse, (25, 25, 25), anchor="mm", align="center", font = txtFont)
today = datetime.now().strftime("%d%m%y")
img.save("../Exports/" + today + ".png")
# DDfile[DDfileValuesLength] = {"Book": TDDValue, "Verse": TDDVerse}
# openDDfile = open("Done DB.json", "w")
# json.dump(DDfile, openDDfile)



# astr = '''The Lord is my shepherd,
# I shall not be in want.'''
# para = textwrap.wrap(astr, width = 30)

# MAX_W, MAX_H = 2000, 4000
# im = Image.open(rm)
# draw = ImageDraw.Draw(im)
# font = ImageFont.truetype("Font/PlayfairDisplay-Regular.ttf", 125)

# current_h, pad = H/2, 20
# for line in para:
#     w, h = draw.textsize(line, font=font)
#     draw.text((W/2, H/2), line, fill=(10, 10, 10), font=font, anchor="mm")
#     current_h += h + pad

# im.save('test.png')