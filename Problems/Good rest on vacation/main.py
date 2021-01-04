# put your python code here
days = int(input())
food_cost = int(input())
one_way_flight_cost = int(input())
cost_of_night = int(input())

print(days * food_cost
      + (days - 1) * cost_of_night
      + one_way_flight_cost * 2)
