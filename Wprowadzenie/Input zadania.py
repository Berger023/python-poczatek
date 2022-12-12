# age_input=input("Ile masz lat?")
# age= int(age_input)
# your_age=age * 12
# print("Masz", age, "lat", "czyli",your_age, "miesięcy")

# walk_distance_input=input("Ile kilometrów przeszedłeś dziś?")
# walk_distance= int(walk_distance_input)
# around_earth_distance = 40075
# days_around_earth = around_earth_distance / walk_distance
# weeks_around_earth = days_around_earth / 7
# print("W takim tempie okrążenie ziemi zajmie Ci", weeks_around_earth, "tygodni")


print("Witaj dzisiaj pokaże Ci o ile się kurwa wzbogadzisz jak weźmiesz lokate w tym jebanym banku")
value_input=input("Ile inwestujesz byczku?")
percent_input=input("Ile procent chcą Ci dać te skurwysyny (%) ?")
time_input=input("Na ile lat oferują Ci te darmozjady lokate?")

value=int(value_input)
percent=int(percent_input)
time=int(time_input)

bank_deposit= value * (1 + percent / 100) ** time
print(f"Jak weźmiesz tą chujową ofertę to po , {time} , latach będziesz miał, {bank_deposit:.2f}")
#













