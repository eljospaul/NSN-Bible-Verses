from instabot import Bot

bot = Bot()
username = "cuty_caty_"
password = "cutycaty@8224"
caption = 'Hello'
img = "D:/Eljos/Bible Verses/static/BGs/Breeze.jpg"

bot.login(username = username, password = password)
bot.upload_photo(img, caption)