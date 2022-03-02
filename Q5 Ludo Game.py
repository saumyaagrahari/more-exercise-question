# print ('PLAYER_NAME',':','Ram' , 'Anshu' , 'Arav' , 'Virat')      # player name

# choose_color = {'Red':['R1','R2','R3','R4'],'Yellow':['Y1','Y2','Y3','Y4'],
# 'Green':['G1','G2','G3','G4'],'Blue':['B1','B2','B3','B4']}

# player_name = input("enter the name:")

# looser_rock_Color = input("take a color:")

# choose_number = (input("enter the number:"))

# # def color():

# i=0
    
# count_1 = 0
    
# while i<len(choose_number):

#     if player_name == 'Ram':

#         if choose_color == 'Red':                    # print("you choose the red color")

#             for i in range('Red'):
                

#                 if choose_number == 6:

#                     count_1+=choose_number

#                     if choose_number == 6:
                            
#                         count_1+=choose_number
                            
#                         if choose_number == 6:

#                             break              
#             i+=1
        










def player2():
    count=0
    a=int(input("take your chance11:"))
    if a==6:
        b=int(input("take another chance22:"))
        if b==6:
            count=count+a+b
            print(count)
        else:
            count=count+a+b
    else:
        print("end")
player_num=int(input("how many player:"))

if player_num<=4:
    c=0
    i=0
    while i<=player_num:
        chance=int(input("take your chance33:"))
        if chance==6:
            chance2=int(input("take another chanceL44:"))
            if chance2==6:
                c=c+chance+chance2
                print(c)
                break        
            else:
                player2()
        else:
            player2()
        i=i+1

if c<=player2:
    print("winner is:",c)
else:
    print("winner is:",player2)


