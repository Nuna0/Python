poetry = """По дороге зимней, скучной
Тройка борзая бежит,
Колокольчик однозвучный
Утомительно гремит дороге."""

print(poetry.find("дороге")) #первый 
print(poetry.rfind("дороге"))  #Послений встречающийся, поисл с конца
print(poetry.count("дороге"))

print(poetry.lower())
print(poetry.upper())
print()
print(poetry.replace("дороге", "улице"))
print(poetry)
print()
poetry = poetry.replace("дороге", "улице")
print(poetry)