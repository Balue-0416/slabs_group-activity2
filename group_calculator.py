# Author: Sinethemba



#This requires users to enter their group name and numbers


group_name = input("Enter your group name: ")
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))



#This is to perform arithmetic operations


addition = num_1 + num_2
float_division = num_1 / num_2
floor_division = num_1 // num_2
modulus = num_1 % num_2


#This shows and prints the data type of each calculation


print("Addition: ", addition, type(addition))
print("Float division: ", float_division, type(float_division))
print("Floor division: ", floor_division, type(floor_division))
print("Modulus: ", modulus, type(modulus))
