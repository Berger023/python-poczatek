
# def calculate_investment_value(initial_value, percentage, years):
#     return initial_value * (1 + percentage / 100) ** years
#
# def ask_for_int_value(message):
#     input_value = input(message)
#     return int(input_value)
#
# def run_investment_calculator():
#     print("Kalkulator wartości lokaty z roczną kapitalizacją")
#
#     initial_value = ask_for_int_value("Jaką kwotę wpłaciłeś/wpłaciłaś?")
#     percentage = ask_for_int_value("Jakie jest oprocentowanie? (%)? ")
#     years = ask_for_int_value("Ile lat trwa lokata? ")
#
#     final_value = calculate_investment_value(initial_value, percentage, years)
#     print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")
#
#     longer_term = years * 2
#     alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
#     print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")
#
# option = None
# while option != 'X':
#     run_investment_calculator()
#     option = input("Aby przerwać wprowadź 'X', wpisz inny znak by kontynuować: ")



#####


def find_best_grade(grades_by_subject):
    best_subject = None
    best_grade = 0
    for subject, grades in grades_by_subject.items():
        best_grade_from_subject = max(grades)
        if best_grade_from_subject > best_grade:
            best_grade = best_grade_from_subject
            best_subject = subject
    return best_grade, best_subject

grades_data = {
    "Historia": [5, 5, 4, 5],
    "Matematyka": [5, 4, 3, 6],
    "Fizyka": [4, 3, 2, 5]
}
the_best_grade, subject = find_best_grade(grades_data)
print(f"Najlepsza uzyskana ocena to {the_best_grade} z {subject}")