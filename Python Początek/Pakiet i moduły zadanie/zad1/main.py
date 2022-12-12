import speed_calculator

running_distance = float(input("Jaki dystans przebiegłeś? "))
running_time = float(input("Ile czasu Ci to zajęło? "))

avg_speed = speed_calculator.avg_speed(running_distance, running_time)
print(f"Przebiegłeś {running_distance}km z średnią prędkością {avg_speed} km/h")