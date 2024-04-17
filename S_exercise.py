#Ask user to input 3 numbers and you have to print average if three numbers using string formatting
 #TRY to take all three comma separated inputs in one line.

#num1, num2, num3 = input("Enter three numbers seperated by , : ") .split(",")
#print(f"Average of three numbers is {(int(num1) + int(num2) + int(num3)) / 3}")

name, char = input("Enter your name and char seperated by comma : ").split(",")
#print(f"The lenght of your name is {len(name)}")
#print(f"The char of your name is {name.lower().count(char.lower())}")



print(f"The char of your name is {name.strip().lower().count(char.strip().lower())}")
