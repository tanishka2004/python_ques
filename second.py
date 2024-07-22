# # strings
# str1 = "this is a string"
# str2 = 'hyee'
# str3 = """hoo"""
# print(str1)
# print(str2)
# print(str3)

# # operations on string (concatenation)
# str4 = "apna"
# str5 = "dekhlo"
# final_str = str4 + str5
# print(final_str)

# # length of str
# print(len(str2))

# # indexing
# print(str2[2])

# # slicing
# print(str1[0:len(str1)])

# # negative index
# str = "Apple"
# print(str[-3:-1])

# # string functions
# print(str2.endswith("yee"))
# print(str2.capitalize())
# print(str2.replace("y" , "o"))
# print(str2.find("i"))
# print(str2.count("e"))

# Ques!
# name = input("Enter your first name:")
# print(name)
# print(len(name))

# conditional statements (if, else, elif)
# age = int(input("enter your age :"))
# print(age)
# if(age >= 18):
#   print("can vote")
# elif(age < 18):
#   print("cannot vote")

# marks = int(input("Enter marks :"))
# print(marks)
# if(marks >= 90) :
#     print("A")
# elif(90 > marks >= 80):
#     print("B")
# elif(80 > marks >= 70):
#     print("C")
# elif(70 > marks >= 50):
#     print("D")
# else:
#     print("fail")

# nesting

# Ques!
# num = int(input("enter a number:"))
# if (num % 2 == 0):
#      print("Even")
# else: 
#      print("odd")

# Ques!
num1 = int(input("enter first no:"))
num2 = int(input("enter secind no:"))
num3 = int(input("enter third no:"))
if( num1 >= num2 and num1 >= num3):
    print(num1)
elif( num2 >= num1 and num2 >= num3):
    print(num2)
else:
    print(num3)
