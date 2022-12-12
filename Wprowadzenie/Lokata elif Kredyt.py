print("Kalkulator:", "1 -> wartości lokaty", "2 -> kredytowy", sep="\n")
option = input("Wybierz opcję: ")

if option == "1":
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

    print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

elif option == "2":
    loan_amount = int(input("Jaka jest kwota kredytu? "))
    interest_rate = float(input("Jakie jest oprocentowanie? "))
    own_contribution = int(input("Jaka jest wartość wkładu własnego? "))
    years = int(input("Jaki jest czas kredytowania (w latach)? "))
    monthly_income = int(input("Jaki jest miesięczny przychód? "))
    monthly_expenditures = int(input("Jaka jest suma miesięcznych wydatków? "))

    installment_value = (loan_amount * interest_rate / 100) / 12 + (loan_amount / (years * 12))
    available_money = monthly_income - monthly_expenditures
    property_value = loan_amount + own_contribution

    own_contribution_part = own_contribution / property_value
    money_over_installment = available_money - installment_value

    matching_higher_own_part = own_contribution_part >= 0.2 and money_over_installment >= 1000
    matching_lower_own_part = own_contribution_part >= 0.1 and money_over_installment >= 2000

    if matching_lower_own_part or matching_higher_own_part:
        print("Można wziąć kredyt")
    else:
        print("Nie można wziąć kredytu")

else:
    print(f"Nie ma takiej opcji: {option}")