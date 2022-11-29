from fileinput import filename
import os
from instabot import Bot
from flask import Flask, flash, render_template, request, redirect, url_for
from datetime import datetime
import random
from PIL import Image, ImageFont, ImageDraw

app = Flask(__name__)
app.secret_key = "nsnbveljos"

rmLi = ["Breeze.jpg", "Cloud.jpg", "Rainy Day.jpg", "Sandstorm.jpg", "Soft Pink.jpg"]
rImg = os.path.abspath("static/BGs/") + random.choice(rmLi)
rImg = rImg.replace("\\", "/").replace("/BGs", "/BGs/")
uncryptPassword = "bibleverses.community.eljos@8224"
today = datetime.now().strftime("%d%m%y")
timeNow = datetime.now().strftime("%I:%M:%S %p")
fileNameImg = os.path.abspath("static/Exports/") + today + ".jpg"
fileNameImg = fileNameImg.replace("\\", "/").replace("/Exports", "/Exports/")
alertUser = False

oldFileNameImg = os.path.abspath("static/Exports/") + today
oldFileNameImg = fileNameImg.replace("\\", "/") + ".REMOVE_ME"

newFileNameImg = os.path.abspath("static/Exports/") + today
newFileNameImg = fileNameImg.replace("\\", "/")
print(oldFileNameImg)
print(newFileNameImg)

@app.route('/', methods =["GET", "POST"])
def Home():
    indexPassword = ""
    if request.method == "POST":
        indexPassword = request.form.get("pass")
        # if indexPassword == uncryptPassword:
        #     auth = True
        #     return redirect("/create")
        # else:
        #     flash("Incorrect Password")
        #     auth = False
    return render_template("/index.html", indexPassword=indexPassword, uncryptPassword=uncryptPassword)

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
            txtFont = ImageFont.truetype("static/Font/NotoSans-Bold.ttf", int(fontSize))
            refFont = ImageFont.truetype("static/Font/NotoSans-Bold.ttf", 70)
            watFont = ImageFont.truetype("static/Font/NotoSans-Medium.ttf", 55)
        except:
            txtFont = ImageFont.truetype("static/Font/NotoSans-Bold.ttf", 150)
            refFont = ImageFont.truetype("static/Font/NotoSans-Bold.ttf", 70)
            watFont = ImageFont.truetype("static/Font/NotoSans-Medium.ttf", 55)
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
        img.save("static/Exports/" + today + ".jpg")
    file_exists = os.path.exists("static/Exports/" + today + ".jpg")
    if file_exists:
        todayPhoto = today
    else:
        todayPhoto = False
    return render_template("/create.html", todayPhoto=todayPhoto)

@app.route('/post', methods =["GET", "POST"])
def PostImg():
    notificationView = "-----"
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        caption = request.form.get("caption")
        bot = Bot()
        bot.login(username = username, password = password, is_threaded=True)
        try:
            up = bot.upload_photo(fileNameImg, caption)
        except:
            up = bot.upload_photo(
                fileNameImg,
                caption = '''🔻 Let People Know about Jesus ✝
                Share Now to your Friends & Family 🙏🏻

                👉🏻 Discover daily bible quotes and verses here

                #bibleversesin
                #Devotional #dailydevotional #christian #christianwoman
                #christianwomen #christianwife #christianwedding #biblejournaling
                #bibleverse #bible #dailyverse #worship #church #dailybibleverse
                #biblequote #biblequotes #testimonials #testimony #testimonial
                #newtestament #oldtestament #christianapparel #christianathlete
                #godlovesyou #godlovesme #christians #christianchurch #christianchurches
                #dailybibleverse''')
        global instaPostID
        instaPostID = up["code"]
        if instaPostID:
            return redirect("/uploaded")
        if up:
            notificationView = "Posted Successfully"
        else:
            notificationView = "Posting..."
        os.rename(oldFileNameImg, newFileNameImg)
    return render_template("/post.html", today=today, notificationView=notificationView)

@app.route('/uploaded', methods =["GET", "POST"])
def Uploaded():
    return render_template("/uploaded.html", instaPostID=instaPostID)

if __name__ == '__main__':
    app.run(debug=True)