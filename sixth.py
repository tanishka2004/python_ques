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
cities = ["delhi", "myssore", "hyderabad", "goa"]
def print_len(cities):
    print(cities)

print_len(cities)

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
def sum(a):
     if(a == 0):
        return 0
     return sum(a - 1) + a
print(sum(5))
