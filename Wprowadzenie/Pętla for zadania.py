# grades = []
# grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
# while grade_input != 'X':
#     grade = int(grade_input)
#     grades.append(grade)
#     grade_input = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
#
# # grades_sum = 0
# # for grade in grades:
# #     grades_sum += grade
# #Łatwiejszy sposób na obliczenie sumy w pythonie vvvvv
# grades_sum = sum(grades)
#
#
# average = grades_sum / len(grades)
# print(f"Twoja średnia wynosi: {average:.2f}")




phone_number = input("Podaj nr telefonu")
phone_number = phone_number.replace("-", "")
formatted_phone_number = ""
for index, digit in enumerate(phone_number):
    if index % 3 == 0 and index != 0:
        formatted_phone_number += "-"
    formatted_phone_number += phone_number[index]

print(f"Twój numer telefonu to: {formatted_phone_number}")

