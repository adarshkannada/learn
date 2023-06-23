def check_array_balance(thelist: list):
    thelist.sort()
    print("the sorted list = ", thelist)
    
    j = len(thelist)
    for i in range(0, j):
        if thelist[i]+thelist[j-1] != 0:
            print(f"the list {thelist} is not balanced")
            break
        j -=1
    else:
        print(f"the list {thelist} is balanced")
    

list1 = [0,-2,-4,4,2,1,-1,10,-10]
list2 = [1,0,-1,2,-3,3,-4,4,5,-5,-2]
list3 = [1,3,4,5,56,3,-1,-3]
all_lists = [list1, list2, list3]
for each in all_lists:
    check_array_balance(thelist=each)
