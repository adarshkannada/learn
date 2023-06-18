number = int(input("enter the positive integer - "))
output_list = []
for num in range(0, number, 1):
    if num % 3 == 0:
        print(" " + "Fizz ", end="")
        output_list.insert(num, "Fizz")
    elif num % 5 == 0:
        print(" ""Buzz ", end="")
        output_list.insert(num, "Buzz")
    elif num % 3 == 0 & num % 5 == 0:
        print(" " + "FizzBuzz ", end="")
        output_list.insert(num, "FizzBuzz")
    else:
        print(str(num) + " ", end="")
        output_list.insert(num, num)
print("\n the final list is: ", output_list)
