from fileinput import filename
import os
from instabot import Bot
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import random
from PIL import Image, ImageFont, ImageDraw

app = Flask(__name__)

rmLi = ["Breeze.jpg", "Cloud.jpg", "Rainy Day.jpg", "Sandstorm.jpg", "Soft Pink.jpg"]
rImg = os.path.abspath("static/BGs/") + random.choice(rmLi)
rImg = rImg.replace("\\", "/").replace("/BGs", "/BGs/")
uncryptPassword = "bibleverses.community.eljos@8224"
today = datetime.now().strftime("%d%m%y")
timeNow = datetime.now().strftime("%I:%M:%S %p")
fileNameImg = os.path.abspath("static/Exports/") + today + ".jpg"
fileNameImg = fileNameImg.replace("\\", "/").replace("/Exports", "/Exports/")
oldFileNameImg = os.path.abspath("static/Exports/") + today + ".jpg"
oldFileNameImg = fileNameImg.replace("\\", "/").replace("/Exports", "/Exports/")
newFileNameImg = os.path.abspath("static/Exports/") + today + ".jpg"
newFileNameImg = fileNameImg.replace("\\", "/").replace("/Exports", "/Exports/")
NotificationView = "-----"

@app.route('/', methods =["GET", "POST"])
def Home():
    if request.method == "POST":
        password = request.form.get("pass")
        if password == uncryptPassword:
            return redirect("/create")
        else:
            return redirect("/")
    return render_template("/index.html")

@app.route('/create', methods =["GET", "POST"])
def Create():
    if request.method == "POST":
        verse = request.form.get("verse")
        reference = request.form.get("reference")
        watermark = request.form.get("watermark")
        fontSize = request.form.get("fontSize")
        W, H = (2000, 2000)
        img = Image.open(rImg).convert("RGB")
        try:
            txtFont = ImageFont.truetype("D:/Eljos/Bible Verses/static/Font/NotoSans-Bold.ttf", int(fontSize))
            refFont = ImageFont.truetype("D:/Eljos/Bible Verses/static/Font/NotoSans-Bold.ttf", 70)
            watFont = ImageFont.truetype("D:/Eljos/Bible Verses/static/Font/NotoSans-Medium.ttf", 55)
        except:
            txtFont = ImageFont.truetype("D:/Eljos/Bible Verses/static/Font/NotoSans-Bold.ttf", 150)
            refFont = ImageFont.truetype("D:/Eljos/Bible Verses/static/Font/NotoSans-Bold.ttf", 70)
            watFont = ImageFont.truetype("D:/Eljos/Bible Verses/static/Font/NotoSans-Medium.ttf", 55)
        verse = verse
        edit = ImageDraw.Draw(img)
        try:
            edit.text((W/2, H/2), verse, (81, 54, 36), font=txtFont, anchor="mm", align="center")
            edit.text((W/2, 1520), reference, (81, 54, 36), align="center", anchor="mm", font = refFont)
            edit.text((W/2, 1800), watermark, (150, 150, 150), align="center", anchor="mm", font = watFont)
        except:
            edit.text((W/2, H/2), "Enter the Verse", (81, 54, 36), font=txtFont, anchor="mm", align="center")
            edit.text((W/2, 1520), "", (81, 54, 36), align="center", anchor="mm", font = refFont)
            edit.text((W/2, 1800), "BibleVerses.in", (150, 150, 150), align="center", anchor="mm", font = watFont)
        img.save("D:/Eljos/Bible Verses/static/Exports/" + today + ".jpg")
    return render_template("/create.html", today=today)

@app.route('/post', methods =["GET", "POST"])
def PostImg():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        bot = Bot()
        bot.login(username = username, password = password, is_threaded=True)
        bot.upload_photo(fileNameImg, caption = "Hello")
        os.rename(oldFileNameImg, newFileNameImg)
    return render_template("/post.html", today=today)

if __name__ == '__main__':
    app.run(debug=True)