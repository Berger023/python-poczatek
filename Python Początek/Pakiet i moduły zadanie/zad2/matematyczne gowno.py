import math

def calculate_c_len(a_len, b_len):
    return math.sqrt(math.pow(a_len, 2) + math.pow(b_len, 2))

a = float(input("Jaka jest długość boku a? "))
b = float(input("Jak jest długość boku b? "))

c = calculate_c_len(a, b)
print(f"Długość przeciwprostokątnej to {c:.2f}")


