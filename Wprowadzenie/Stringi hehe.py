# name=input("Jak masz na imię?")
# print(f"Twoje imię ma aż {len(name)} liter!")

# city=input("Gdzie mieszkasz?")
# print(f"Jak miło że mieszkasz w: {city.title()}")

ford = "ab100100"
audi = "EEE 123123"
citroen="Zk-300300"
honda="AB210210"

ford=ford.upper()
audi=audi.replace(" ","")
citroen=citroen.upper().replace("-","")

print(f"Ford:{ford}")
print(f"Audi:{audi}")
print(f"Citroen:{citroen}")
print(f"Honda:{honda}")