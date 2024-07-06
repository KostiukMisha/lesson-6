numbers = range(1, 10)

divisible_by_2 = []
divisible_by_3 = []
not_divisible_by_2_and_3 = []

for number in numbers:
    if number % 2 == 0:
        divisible_by_2.append(number)
    if number % 3 == 0:
        divisible_by_3.append(number)
    if number % 2 != 0 and number % 3 != 0:
        not_divisible_by_2_and_3.append(number)
        
print( divisible_by_2)
print( divisible_by_3)
print( not_divisible_by_2_and_3)
