import db

db.addKey("bamuel", 2)
print(db.readKey("bamuel"))
db.addKeyUnsafe("len", 4)
print(db.readKeyUnsafe("len"))