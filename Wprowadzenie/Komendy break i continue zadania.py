# subjects = ["matematyka", "fizyka", "język polski", "język angielski", "historia"]
# grades = []
# for subject in subjects:
#     grade = int(input(f"Jaka jest Twoja ocena końcowa z przedmiotu {subject}? "))
#     grades.append(grade)
#
# for grade in grades:
#     if grade == 1:
#         print("Niestety...")
#         break
# else:
#     print("Gratulację! Zdałeś do następnej klasy :) ")






# print("Kalkulator budżetu miesięcznego")
# expenditures = {}
#
# while True:
#     category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
#     if category_name == "X":
#         break
#     expenditures[category_name] = []
#
#     while True:
#         expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X' ")
#         if expenditure == "X":
#             break
#
#         expenditure_value = float(expenditure)
#         expenditures[category_name].append(expenditure_value)
#
# total_expenditures = 0
# for category_expenditures in expenditures.values():
#     total_expenditures += sum(category_expenditures)
#
#
# expenditure_percentage = {}
# for category_name, category_expenditures in expenditures.items():
#     total_category_expenditures = sum(category_expenditures)
#     expenditure_percentage[category_name] = total_category_expenditures * 100 / total_expenditures
#
# most_important_category = None
# most_important_category_percentage = 0
# for category, percentage in expenditure_percentage.items():
#     if percentage > most_important_category_percentage:
#         most_important_category_percentage = percentage
#         most_important_category = category
#
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")
#
# for category, percentage in expenditure_percentage.items():
#     print(f"Na {category} wydajesz {percentage:.0f}% miesięcznych wydatków")
#


numbers = [1, 3, 4, 2, 3, 4, 56, 234, 2, 5231, 54, 62, 523, 451, 34]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)