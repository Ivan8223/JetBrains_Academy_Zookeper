# put your python code here
hours_before = int(input())
minutes_before = int(input())
seconds_before = int(input())
hours_after = int(input())
minutes_after = int(input())
seconds_after = int(input())

print(((hours_after - hours_before) * 60
       + (minutes_after - minutes_before)) * 60
      + seconds_after - seconds_before)
