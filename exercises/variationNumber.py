user_number = int(input("Enter number: "))
variation = int(input("Enter a variation: "))

result1 = user_number - variation
result2 = user_number + variation + 1

for result in range (result1, result2):
    print(result)
