def best_grades(grades, best_grades_number=1):
    grades.sort(reverse=True)
    if best_grades_number < len(grades):
        return grades[:best_grades_number]
    print("Nie można zwrócić więcej ocen niż jest na liście. Zostaną zwrócone wszystkie...")
    return grades

math_grades = [1, 3, 4, 1, 2, 5, 4]
print(best_grades(math_grades))
print(best_grades(math_grades, 4))
print(best_grades(math_grades, best_grades_number=4))