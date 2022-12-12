# Słownik szkolny
# school={
#     "Matematyka": [4,3,2,6],
#     "j.Polski": [5,3,3,4],
#     "j.Angielski": [6,5,5,4],
#     "j.Niemiecki": [3,3,2,4],
#     "WF": [6,6,6,5],
#     "Biologia": [4,4,5,3]
# }
# print(school)
# keys = list(school.keys())
# values = list(school.values())
# print(keys)
# print(values)

#Drzewo

# my_family={
#     "first_name": "Jakub",
#     "last_name": "Kierzek",
#     "age": 21,
#     "birthday": "08-07-2001",
#     "parents":[
#         {
#             "first_name": "Agnieszka",
#             "last_name": "Kierzek",
#             "age": 45,
#             "birthday": "20-10-1977",
#             "parents":[]
#         }
#     ]
#
# }
# print(my_family)


print("Ile miesięcznie wydajesz na")
food = float(input("jedzenie? "))
bills = float(input("opłaty? "))
fun = float(input("rozrywkę? "))
other = float(input("inne? "))


total_expenditures = food + bills + fun + other
expenditures_percentage = {
    "jedzenie": food * 100 / total_expenditures,
    "opłaty": bills * 100 / total_expenditures,
    "rozrywka": fun * 100 / total_expenditures,
    "inne": other * 100 / total_expenditures,
}

selected_category = input("Wybierz jedną z kategorii wydatków (jedzenie/opłaty/rozrywka/inne): ")
print(f"Na {selected_category} wydajesz {expenditures_percentage[selected_category]:.0f}% wszystkich wydatków")
