from tinydb import TinyDB, Query

db = TinyDB('To Do DB.json')
db.insert({"Book": "Psalm 23:1", "Verse": "The LORD is my shepherd,\nI shall not be in want."})
print(db.all())