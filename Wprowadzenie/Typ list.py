# favourite_sports=[
#     "Piłka nożna",
#     "Koszykówka",
#     "Siatkówka",
#     "Pływanie",
#     "Łyżwiarstwo",
# ]
# print(favourite_sports)
# print("Ulubiony sport to:",favourite_sports[0])
# print("Drugi ulubiony sport to:", favourite_sports[1])
# print("Ostatni sport z mojej listy to:", favourite_sports[-1])
#
# favourite_sports.append("Bieganie")
# print(favourite_sports)
# favourite_sports[-1]=("Jazda na rowerze")
# print(favourite_sports)

#
# favourite_dishes = []
# dish = input("Jakie jest Twoje ulubione danie nr 1?")
# favourite_dishes.append(dish)
# dish = input("Jakie jest Twoje ulubione danie nr 2?")
# favourite_dishes.append(dish)
# dish = input("Jakie jest Twoje ulubione danie nr 3?")
# favourite_dishes.append(dish)
# print("Twoje ulubione dania to:", favourite_dishes)
#
# # ALBO
#
dishes=input("Wymień 3 potrawy które lubisz rozdzielając je przecinkiem")
favourite_dishes=dishes.split(",")
print(favourite_dishes)


#
# phone_number = input("Jaki jest Twój numer telefonu?")
# phone_number = phone_number.replace("-","")
# public_digits = phone_number[:6]
# number_of_private_digits = len(phone_number) - 6
# private_digits = "-" * number_of_private_digits
# anonymous_number = f"{public_digits}{private_digits}"
# print("Zanonimizowany numer:", anonymous_number)
