# def numbers(list1,list_20):
#     counter = 0
#     while counter < len(list1):
#         item = list1[counter]
#         if item > 20:
#             # list1.remove(item)
#         # else:
#         #     counter += 1
#         # return list1
#                 list1 = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
# list_20 = numbers (list1)
# print ("Initial list",list1)
# print ("List that doesn't contain numbers greate than 20", list_20)


def numbers_less_than_twenty(list):
    counter = 0
    while counter < len(list):
        item = list[counter]
        if item > 20:
            list.remove(item)
        else:
            counter += 1
        return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

print ("Initial list", num_list)

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("List that doesn't contain numbers greate than 20", num_list_sub_20)

