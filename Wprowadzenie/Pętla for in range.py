print("Kalkulator wartości lokaty z roczną kapitalizacją")

intitial_value_input = input("Jaką kwotę wpłaciłeś? ")
intitial_value = int(intitial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

for year_number in range(1, years + 1):
    investment_value = intitial_value * (1 + percentage / 100) ** year_number
    print(f"Po {year_number} latach Twoja lokata będzie warta {investment_value:.2f}")