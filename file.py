import os
from datetime import datetime

today = datetime.now().strftime("%d%m%y")
print(today)
timeNow = datetime.now().strftime("%I:%M:%S %p")
timeNow = timeNow.replace(":", "")
timeNow = timeNow.replace(" PM", "")
print(timeNow)
fileNameImg = os.path.abspath("static/Exports/") + today + timeNow + ".jpg"
fileNameImg = fileNameImg.replace("\\", "/").replace("/Exports", "/Exports/")
print(fileNameImg)
alertUser = False

oldFileNameImg = os.path.abspath("static/Exports/") + today
oldFileNameImg = fileNameImg.replace("\\", "/") + ".REMOVE_ME"

newFileNameImg = os.path.abspath("static/Exports/") + today
newFileNameImg = fileNameImg.replace("\\", "/")
print(oldFileNameImg)
print(newFileNameImg)