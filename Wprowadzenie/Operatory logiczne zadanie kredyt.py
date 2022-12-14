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
