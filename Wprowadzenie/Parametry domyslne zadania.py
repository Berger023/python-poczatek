# def value_with_tolerance(value, tolerance_percentage=10):
#     tolerance_value = tolerance_percentage * value / 100
#     return [value - tolerance_value, value + tolerance_value]
#
# print(value_with_tolerance(value=100))
# print(value_with_tolerance(value=100, tolerance_percentage=40))




def add_people_to_classes(names_str, participants=None):
    if participants is None:
        participants = []
    names = names_str.split(',')
    for name in names:
        participants.append(name)
    # participants += names
    return participants

attendees_names = "Ola,Bob,Ala,Kuba"
monday_course_participants = add_people_to_classes(attendees_names)
print(monday_course_participants)
attendees_names = "Paweł,Dominika"
monday_course_participants = add_people_to_classes(attendees_names, participants=monday_course_participants)
print(monday_course_participants)


attendees_names = "Ania,Krzysztof"
friday_course_participants = add_people_to_classes(attendees_names)
print(friday_course_participants)