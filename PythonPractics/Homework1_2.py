# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

# n = 6 -> 1 4 1  
# n = 24 -> 4 16 4    
# n = 60 -> 10 40 10 
n = 60
peter = n//6
kate = (n//3)*2

print(f"-> {peter} {kate} {peter}")