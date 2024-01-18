bus_count = 50
full_gas = 100
way = 0

while full_gas != 0 and bus_count != 0:
    way += 1
    full_gas -= 1
    bus_count //= 2  
    if bus_count >= 1:
        full_gas += 1
    print('Way=', way, ' BUS=', bus_count)

print("Методом перелива топлива удастца пероехать не менее:", way * 50+50)  
