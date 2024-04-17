# name = "   Pratiksha   Kandel    "
# dots = ".............."
# print(name.lstrip() + dots) # deleate space in left side
# print(name.rstrip() + dots)
# print(name.strip() + dots)
# print(name.replace(" ", "") + dots)


# replace method
mango = "It is a very hummy fruits and perfect for summer and is good for Chilren"
print(mango.replace("is", "was", 2))

#find method
is_pos1 = mango.find("is")
print(is_pos1)
is_pos2 = mango.find("is", is_pos1 + 1)
print(is_pos2)