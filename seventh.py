# file I/O
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# data2 = f.readline() #read line one by one

# f = open("demo.txt", "w")
# f.write("hyeeeeeeeeeee")

# f.close()

# f = open("demo.txt", "a")
# f.write("tomorrow I will learn reactjs")
# f.write("yes")
# f.close()

f = open("demo.txt", "r+")
f.write("okay")
print(f.read())
f.close()

# f = open("demo.txt", "w+") 
# print(f.read())
# f.close()

# f = open("sample.txt", "w")


# with syntax
# with open("demo.txt", "r")as f:
#     data = f.read()
# print(data)

# with open("demo.txt", "w")as f:
#    f.write("new data")

# to delete a file
# import os
# os.remove("sample.txt")

# Ques!
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/O\n")
    f.write("using java\nI like programming in java")
    
