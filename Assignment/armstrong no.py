import math
number = input("Please Enter the number : ")
l = [ int(i) for i in (number)]
new_list = list(map(lambda x : x**3 , l))
if sum(new_list) == int(number):
    print(f"Yes the number {number} is an Armstrong Number")
else :
    print(f"No the number {number} is not an Armstrong Number")
