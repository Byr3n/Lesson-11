num=int(input("Enter a number"))
sum=0
tam=num
while tam>0:
    digit=tam%10
    sum+=digit**3
    tam//=10
if num==sum:
    print("it's an Armstrong Number")
else:
    print("It's not an Armstrong Number")
