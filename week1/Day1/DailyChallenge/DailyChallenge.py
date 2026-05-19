#Challenge 1 
#Instruction 
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length

user_number=int(input("enter a number :"))
user_length=int(input("enter a length :"))
multiples=[user_number]
for i in range(user_length):
    multiples.append(multiples[-1]+user_number)
print(multiples)
#============================divider========================================

#Challenge 2
#Instruction

user_string = input("enter a string : ")
user_string_list = list(user_string)

i = 1

while i < len(user_string_list):
    if user_string_list[i] == user_string_list[i - 1]:
        user_string_list.pop(i)
    else:
        i += 1

print("".join(user_string_list))