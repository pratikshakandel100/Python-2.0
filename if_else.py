# winning_number = 65
# num = int(input("Enter any number : "))
# if num == winning_number:
#     print("Congratulation! You won.")
# else:
#     if num >= 100 :
#       print("Your number is too high.")
#     else: num <= 15 
#     print("Your number is too low.")

name, age = input("Enter your name and age : ").split(",")
age = int(age)
if name[0] == "a" or "A" and age > 10:
    print("You can play cocoa")
else:
    print("You can't play cocoa.")
