shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem ")
shopping_list = shopping_elements.split(",")

if "chleb" in shopping_list or "bułki" in shopping_list:
    print("Jest pieczywo")


#
phone_number = input("Podaj swój nr telefonu ")
if "0" in phone_number:
    print("Twój numer zawiera zero")
else:
    print("Nie zawiera zera")

value = 30

if value is True:
    print("To prawda")
elif value is False:
    print("To fałsz")
elif value is None:
    print("To nic")
else:
    print("To inna wartość")

