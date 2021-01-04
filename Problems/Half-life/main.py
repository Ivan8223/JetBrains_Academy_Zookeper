initial_quantity = int(input())
final_quantity = int(input())
days = 12

while initial_quantity / 2 >= final_quantity:
    initial_quantity /= 2
    days += 12

print(days)
