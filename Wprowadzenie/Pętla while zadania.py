# number = int(input("Podaj liczbę parzystą: "))
# try_number = 1
# while try_number < 10 and number % 2 != 0:
#     number = int(input("Spróbuj jeszcze raz. Podaj liczbę parzystą: "))
#     try_number += 1

phone_number = input("Podaj nr telefonu")
phone_number = phone_number.replace("-", "")
formatted_phone_number = ""
digit_index = 0
while digit_index < len(phone_number):
    if digit_index % 3 == 0 and digit_index != 0:
        formatted_phone_number += "-"
    formatted_phone_number += phone_number[digit_index]
    digit_index += 1

print(f"Twój numer telefonu to: {formatted_phone_number}")


dishes = input("Jakie są Twoje ulubione dania? (Wypisz rozdzielając je przecinkiem) ")
favourite_dishes = dishes.split(",")

dish_index = 0
while dish_index < len(favourite_dishes):
    print(f"Ulubione danie numer {dish_index}: {favourite_dishes[dish_index]}")
    dish_index += 1