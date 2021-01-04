value = int(input())
years = 0

while value < 700000:
    value += value * 0.071
    years += 1

print(years)
