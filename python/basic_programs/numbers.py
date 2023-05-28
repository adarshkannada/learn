number = int(input("enter the number to be reversed"))
def reverse_the_number(number):
    print("the number before reversing:  %d " %number)
    reverse = 0
    while(number != 0):
        reverse = reverse *10 + number%10
        number = number // 10
    print("the reversed number is:  %d " %reverse)
    
# reverse_the_number(number = number)
