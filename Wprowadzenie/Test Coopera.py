age = int(input("Ile masz lat? "))
gender = input("Jesteś mężczyzną czy kobietą? (M/K) ")
result = int(input("Jaki był Twój wynik w teście 12 minut biegu (ile metrów)? "))

if age == 8:
    if gender == "M":
        if result >= 2190:
            print("Bardzo dobrze")
        elif result >= 1810:
            print("Dobrze")
        elif result >= 1420:
            print("Średnio")
        elif result >= 1050:
            print("Źle")
        else:
            print("Bardzo źle")
    else:
        if result >= 2010:
            print("Bardzo dobrze")
        elif result >= 1670:
            print("Dobrze")
        elif result >= 1320:
            print("Średnio")
        elif result >= 990:
            print("Źle")
        else:
            print("Bardzo źle")


