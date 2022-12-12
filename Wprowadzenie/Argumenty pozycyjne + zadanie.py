def add_two_number(first_num, second_num):
    print(f"first_num: {first_num}")
    print(f"second_num: {second_num}")
    return first_num + second_num

print(add_two_number(2, 5))
print(add_two_number(5, 2))

####


def avg_speed(distance, time):
    return distance / time

def run_avg_speed_calculator(vahicle_name):
    distance = float(input(f"Ile km pokonałeś za pomocą {vahicle_name}? "))
    time = float(input("Ile godzin Ci to zajęło? "))
    average_speed = avg_speed(distance=distance, time=time)
    print(f"Twoja średnia prędkość przemieszczania się za pomocą {vahicle_name} to {average_speed:.2f} km/h ")

run_avg_speed_calculator(vahicle_name="biegu")
run_avg_speed_calculator(vahicle_name="roweru")
run_avg_speed_calculator(vahicle_name="samochodu")