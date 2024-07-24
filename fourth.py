# Dictionary
# info = {
#     "key" : "value",
#     "name" : "Tanishka",
#     "age" : 20,
#     "subjects" : ["java", "python"],
#     "topics" : ("dic" , "sets")
# }

# print(info)
# print(type(info))

# they are unordered, mutable, don't allow duplicate krys
# print(info["age"])
# print(info["topics"])
# info["name"] = "Tanishkajain"  #overwrite
# print(info)

# null_dict = {}
# null_dict["key"] = "value"
# print(null_dict)

# nested dict
# stu = {
#     "name" : "Riya singh" ,
#     "subjects" : {
#         "phy" : 50,
#         "chem" : 45,
#         "math" : 56
#     }
# }
# print(stu)
# print(stu["subjects"])
# print(stu["subjects"]["chem"])

# dict methods
# print(len(stu))
# print(stu.keys())
# print(stu.values())
# print(list(stu.items()))
# pairs = list(stu.items())
# print(pairs[1])
# print(stu.get("name"))
# new_dict = {"city" : "delhi", "age": 20}
# stu.update(new_dict)
# print(stu)

# sets

# collection = {1,2,2,3,3,"hye"}
# print(collection)
# print(type(collection))
# print(len(collection))

# null_set = set() #syntax for empty set
# print(type(null_set))

# set methods

# collection.add(4)
# print(collection)
# collection.remove(2)
# print(collection)
# collection.clear()
# print(collection)
# print(collection.pop()) 

# set1 = {1,2,3,5}
# set2 = {3,4,5,6}
# print(set1.union(set2))
# print(set1)
# print(set1.intersection(set2))

# Ques!
# my_dict = {
#     "table" : ["a piece of furniture" , "list of facts"],
#     "cat" : "a small animal"
# }
# print(my_dict)

# Ques!
# set1 = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(len(set1))

# Ques!
# my_dict = {}
# subj1 = int(input("enter marks of phy:"))
# my_dict.update({"phy" : subj1})
# subj2 = int(input("enter marks of chem:"))
# my_dict.update({"chem" : subj2})
# subj3 = int(input("enter marks of maths:"))
# my_dict.update({"maths" : subj3})
# print(my_dict)

# Ques!
# set1 = {9,"9.0"}
# print(set1)
 
