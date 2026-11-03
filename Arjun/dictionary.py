# variables

# name = "Arjun"

# list

# name = ["Arjun","Monty","Aman",10,33.33]


# we have to store the name,age,student_id for every single student in a class (total 15 students are in class)

# grade_9 = ["Arjun",10,"001","Monty",10,"002","Aman",11,"009"]

# this is not a right technique to store this data

# why?

# these informations are missing the labeling 

# dictionary


# grade_9 = [
#     {
#     "name":"Arjun",
#     "age":10,
#     "student_id":"001",
#     },
#     {
#     "name":"Arjun",
#     "age":10,
#     "student_id":"009",
#     },
#     {
#     "name":"Arjun",
#     "age":10,
#     "student_id":"010",
#     },
# ]


students = [
    {
        "name" : "Arjun",
        "age" : 12,
        "studen_id" : "001",
    },
    {
        "name" : "Sam",
        "age" : 11,
        "student_id" : "002",
    },
    {
        "name" : "Bob",
        "age" : 12,
        "student_id" : "003",
    },
    {
        "name" : "Joe",
        "age" : 9,
        "student_id" : "004",
    },
    {
        "name" : "Carlos",
        "age" : 14,
        "student_id" : "005",
    },
    {
        "name" : "Adrien",
        "age" : 12,
        "student_id" : "006",
    },
    {
        "name" : "Dan",
        "age" : 13,
        "student_id" : "007",
    },
    {
        "name" : "Danny",
        "age" : 11,
        "student_id" : "008",
    },
    {
        "name" : "Sammy",
        "age" : 12,
        "student_id" : "009",
    },
    {
        "name" : "Jim",
        "age" : 13,
        "student_id" : "010"
    }
    ]

# dict1 = students[0]

# print(dict1)

# key:value
# this is the basic structure of a dictionary to store the data

# How to access the data from dictionary
# dict1 = {
#         "name" : "Jim",
#         "age" : 13,
#         "student_id" : "010"
#     }

# print(dict1.keys())
# print(dict1.values())

# print(dict1["name"])
# print(dict1["age"])

# print(dict1)

# How to update the data in dictionary
# dict1["student_id"] = "001"
# print(dict1)

# How to add new data in dictionary
# dict1["grade"] = 10
# print(dict1)

# dict1.update({"grade":10})
# print(dict1)


# How to remove the data from dictionary
# dict1.pop("age")
# print(dict1)


# How to use the dictionary with loop

dict1 = {
        "name" : "Jim",
        "age" : 13,
        "student_id" : "010"
    }

for i,j  in dict1.items():
    print(i,j)


# -----------------------------------------------

# Exercise

# Create a code to update the values in dictionary

# school_data = {
#     "no_of_rooms":20,
#     "principal_name": "Richa ghosh",
#     "vice-principle":"Atul mehra",
#     "highest_grade": 12,
#     "lowest_grade":5,
#     "Average_Result_2025": 89.77
# }


# Create a code to update as follows:

# update no of rooms to 30
# update the lowest grade to 3
# add the new data as bus service as True
# delete the vice-pricipal data 
# update the principle data to Sameer bhardwaj

# Create a code to make a dictionary using input()
school_data = {}

room = int(input("Enter the number of rooms: "))
school_data['no_of_rooms'] = room