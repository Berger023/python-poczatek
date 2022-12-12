# #Słownik polsko angielski
# polish_to_english = {
#     "amnezja": "amnesia",
#     "aktywista": "avtivist",
#     "burza": "storm"
# }
# print("Słownik polsko angielski:", polish_to_english)
#
# #dostęp za pomocą klucza

# print(f"Po polsku 'burza' to po angielsku '{polish_to_english['burza']}'")


teacher = {
    "first_name": "Jan",
    "last_name": "Kowalski",
    "age": 45,
    "contract": {
        "sign_date": "23-11-2018",
        "salary": 3500
    }
}
print(teacher)

keys=list(teacher.keys())
values=list(teacher.values())
print(keys)
print(values)