import statistics

orders = [2.50, 4.50, 2.00, 2.75, 2.50, 5.00, 8.00, 2.25]

average = statistics.mean(orders)

print("The average coffee order price today is $" + str(round(average, 2)))



orders = (2.50, 4.50, 2.00, 2.75, 2.50, 5.00, 8.00, 2.25)

average = statistics.mean(orders)

print("The average coffee order price today is $" + str(round(average, 2)), ".")
 

temperatures = [-12, -14, -2, -5, -8, -4, -9]

average = statistics.mean(temperatures)

print("The average of this week's lowest daily temperatures is", round(average, 2), "degrees Celsius.")