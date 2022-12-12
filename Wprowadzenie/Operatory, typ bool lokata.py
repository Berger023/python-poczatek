#
# apples_price = float(input("Ile średnio kosztują jabłka? "))
# bananas_price = float(input("Ile średnio kosztują banany? "))
# pears_price = float(input("Ile średnio kosztują gruszki? "))
#
# print(f"Czy jabłka są droższe od bananów? \t\t\t\t\t\t\t {apples_price > bananas_price}")
# print(f"Czy banany są droższe od jabłek? \t\t\t\t\t\t\t {bananas_price > apples_price}")
# print(f"Czy banany kosztują tyle co gruszki? \t\t\t\t\t\t {bananas_price == pears_price}")
# print(f"Czy jabłka są droższe lub w tej samej cenie co gruszki? \t {apples_price >= pears_price}")


# shopping_elements = input("Wprowadź listę zakupów, rozdzielając poszczególne elementy przecinkiem ")
# shopping_list = shopping_elements.split(",")
#
# is_shopping_list_long = len(shopping_list) > 4
# print(f"Czy uważam, że twoja lista zakupów jest długa? {is_shopping_list_long}")


print("Kalkulator wartości lokaty z roczną kapitalizacją")

intitial_value_input = input("Jaką kwotę wpłaciłeś? ")
intitial_value = int(intitial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

final_value = intitial_value * (1 + percentage / 100) ** years
capital_growth = final_value - intitial_value
capital_growth_percentage = (capital_growth / intitial_value) * 100

print("Po", years, "latach Twoja lokata będzie warta", final_value)
print(f"Czy wartość Twojej lokaty wzrośnie w tym czasie o 10% lub więcej? {capital_growth_percentage >= 10}")



