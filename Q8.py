list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
new_list = []
i=0
while i <len(list1):
    if len(list1)>len(list2):
        if list1[i] not in list2:
            new_list.append(list1[i])
    i+=1
print(new_list)

# i=0
# while i<=len(list1):
#     if list1[i] not in list2:
#         new_list.append(list2[i])
#     i+=1
# print(new_list)
