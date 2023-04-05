""" comprehensions
Performing mathematical operations on the entire list
"""
lista = [2, 3, 5, 7, 11]
squared_list = [x**2 for x in lista]
squared_dict = {x:x**2 for x in lista}
print(squared_dict)
print(squared_list)

# Performing conditional filtering operations on the entire list
listb = [2, 3, 5, 7, 11]
squared_list = [x**2 for x in listb if x%2 == 0]
print(squared_list)

