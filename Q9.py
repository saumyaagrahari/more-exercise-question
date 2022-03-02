num = int(input("enter the number:"))
n = num
rem = 0
sum = 0
while num>0:
    rem = num % 10
    sum+=rem
    num//=10
    if n % sum == 0:
        print("it is a harshad number:",num)
    else:
        print("it is not harshad number:",num)