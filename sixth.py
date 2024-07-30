# Functions
# functions definition
# def calsum(a , b): #parameters
#     sum = a + b
#     print(sum)
#     return sum

# calsum(2 , 3) #function call; arguments

# average of 3 no.
# def avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg
# avg(1,2,3)

# def area(a,b,c):
#     sum = a+b+c
#     div = sum/3
#     print(div)
#     return(div)
# area(5,4,6)

# default parameters
# def calsum(a=1 , b=1): 
#     sum = a + b
#     print(sum)
#     return sum
# calsum()

# Ques!
# def facto(a):
#     fact = 1
#     i = 1
#     while i <= a:
#         fact *= i
#         i += 1
#     print(fact)
# facto(5)

# Ques
# def cal_inr(a):
#     i = a*83
#     print(i)
# cal_inr(2)

# Ques!
# def check(a):
#     if(a % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# check(54)    

# Recursion
# recursive function
# def show(a):
#     if(a == 0): #base case -> stopping condition
#         return
#     print(a)
#     show(a-1)
# show(3)

# def fact(a):
#     if(a == 1 & a == 0):
#         return 1
#     return fact(a - 1) * a
# print(fact(5))

# Ques!
# def sum(a):
#      if(a == 0):
#         return 0
#      return sum(a - 1) + a
# print(sum(6))

# Ques!
# def lis(list,idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     lis(list, idx+1)
# fruits = "mango" , "litchi", "apple", "grapes"
# lis(fruits)

# x = int(input("Enter the 1st number"))
# y = int(input("Enter the 2nd number"))
# sum = x + y
# product = x * y
# print("The sum of both numbers are:", sum)
# print("The product of both numbers are:", product)

# check mul and sum of two no.
# def mul_sum_calc(num1,num2):
#     product = num1*num2
#     if(product <= 1000):
#         return product
#     else:
#         return num1 + num2
# print(mul_sum_calc(20,30))
# print(mul_sum_calc(40,30))

# print and sum the prev and current no.
# previous_num = 0
# for i in range(1,11):
#     sum = previous_num + i
#     print("current no", i, "previous no", previous_num, "sum", sum)
#     previous_num = i

# print only even index element of a string
# string = input("enter your string: ")
# print("original string", string)
# size = len(string)
# for i in range(0, size - 1, 2):
#     print(string[i])

# remove first n char from string
# def remove_chars(word, n):
#     x = word[n:]
#     return x

# print(remove_chars("helloworld", 4))
