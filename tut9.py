# symbols of data types
# ()Tuple
# {}Dictionary
# []Lists

# list1 = [["harry",1],["larry",2],["carry",45],["Marie",250]]
# dict1 = dict(list1)
# print(dict1)

# # print(list1[0], list1[1])
# for item, lollypop in list1:
#     print(item,"and lolly is",lollypop)

item = [int,float,"harry",5,4,22,3,21,64,25,89]

for key in item:
    if str(key).isnumeric() and key>6:
        print(key)