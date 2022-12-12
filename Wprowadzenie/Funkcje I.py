# def put_a_brick():
#     print("-", sep="", end="")
#
# #Funkcja może wołać inną funkcję
#
# def build_a_wall():
#     wall_length = 10
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_a_wall()
#
#
# def build_a_wall(wall_length):
#     for brick in range(wall_length):
#         put_a_brick()
#     print()
#
# build_a_wall(20)
# build_a_wall(10)
# build_a_wall(35)



def calculate_investment_value(initial_value, percentage, years):
    return initial_value * (1 + percentage / 100) ** years

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value_input = input("Jaką kwotę wpłaciłeś? ")
initial_value = int(initial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

final_value = calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

longer_term= years * 2
alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")