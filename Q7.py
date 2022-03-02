list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
new_list = [] 
i=0
while i<len(list2):
    if len(list2)>len(list1):
        if list2[i] in list1:
            new_list.append(list2[i])
    i+=1
print(new_list)



































# a = ['abhey']
# b = ['saumya']
# c=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
        
