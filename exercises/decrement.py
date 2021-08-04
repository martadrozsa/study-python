user_number = int(input("Enter starting number: "))
step = int(input("Enter step value: "))
target_value = int(input("Enter target value: "))

number = user_number
if user_number < target_value:
   print("Invalid stating number!")

else:
    while number > target_value:
        number = number - step

        print(number)