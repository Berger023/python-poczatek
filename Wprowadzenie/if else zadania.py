# if 7 > 3:
#     print("Masz racje skurczybyku")

# name = input("Jak się nazywasz? ")
# print(f"Miło Cię poznać {name} ")
#
# if len(name) >= 7:
#     print(f"{name} to całkiem długie imię!")
# else:
#     print(f"{name} to raczej krótkie imię!")


# if 7 < 3:
#     print("To oczywiste!")
# else:
#     print("To się nie wydarzy")

#1111111111111


# computer_price = float(input("Ile średnio kosztuje komputer? "))
# car_price = float(input("Ile kosztuje typowy samochód? "))
# bike_price = float(input("Ile kosztuje typowy rower? "))
#
# if computer_price > car_price:
#     print("Komputer jest droższy od samochodu")
# else:
#     print("Komputer jest tańszy od samochodu")
#
# if bike_price > computer_price:
#     print("Komputer jest tańszy od roweru")
# else:
#     print("Komputer jest droższy od roweru")
#
# if bike_price == car_price:
#     print("Samochód kosztuje tyle co rower")
# else:
#     print("Samochód nie kosztuje tyle co rower")
#
# #22222222222222222


# shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem ")
# shopping_list = shopping_elements.split(",")
#
# if len(shopping_list) > 4:
#     print("Ale długa lista")
# else:
#     print("Ale krótka lista")

#33333333333333333


# print("Ile miesięcznie wydajesz na ")
# food = float(input("jedzenie? "))
# bills = float(input("opłaty? "))
# fun = float(input("rozrywkę? "))
# other = float(input("inne? "))
#
#
# total_expenditures = food + bills + fun + other
# expenditures_percentage = {
#     "jedzenie": food * 100 / total_expenditures,
#     "opłaty": bills * 100 / total_expenditures,
#     "rozrywka": fun * 100 / total_expenditures,
#     "inne": other * 100 / total_expenditures,
# }
#
# most_important_category = "jedzenie"
#
# if expenditures_percentage["rozrywka"] > expenditures_percentage[most_important_category]:
#     most_important_category = "rozrywka"
# if expenditures_percentage["opłaty"] > expenditures_percentage[most_important_category]:
#     most_important_category = "opłaty"
# if expenditures_percentage["inne"] > expenditures_percentage[most_important_category]:
#     most_important_category = "inne"
#
# print(f"Najwięcej wydajesz na {most_important_category} - {expenditures_percentage[most_important_category]:.0f}% wszystkich wydatków")


#4444444

# math_grade = int(input("Jaka jest Twoja ocena końcowa z matematyki? "))
# physics_grade = int(input("Jaka jest Twoja ocena końcowa z fizyki? "))
# polish_grade = int(input("Jaka jest Twoja ocena końcowa z języka polskiego? "))
# english_grade = int(input("Jaka jest Twoja ocena końcow z języka angielskiego? "))
# history_grade = int(input("Jaka jest Twoja ocena końcowa z historii? "))
#
# number_of_failures = 0
# if math_grade < 2:
#     number_of_failures = number_of_failures + 1
# if physics_grade < 2:
#     number_of_failures = number_of_failures + 1
# if polish_grade < 2:
#     number_of_failures = number_of_failures + 1
# if english_grade < 2:
#     number_of_failures = number_of_failures + 1
# if history_grade < 2:
#     number_of_failures = number_of_failures + 1
#
# if number_of_failures == 0:
#     print("Gratuluje! Zdałeś do następnej klasy!")
# else:
#     if number_of_failures == 1:
#         average = (math_grade + physics_grade + polish_grade + english_grade + history_grade) / 5
#         if average > 3.5:
#             print("Gratuluję! Zdałeś do następnej klasy!")
#         else:
#            print("Niestety...")
#     else:
#         print("Niestety...")

#5555555

name = input("Jak masz na imię? ")

if name[-1] == "a":
    print("Jesteś kobietą")
else:
    print("Jesteś mężczyzną")