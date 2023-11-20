given_num=int(input())
b=1
for number in range(1,given_num+1):
    for c in range(1,(given_num-number)+1):
        print(" ",end="")
    for j in range(0,number):
        if j==0 :
            b=1
        else:
            b=b*(number-j)//j
        print(b,end=" ")
    print()