#printing pattrn
'''
def star_pattrn(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
star_pattrn(5)'''
#printing pattren of numbers
n = int(input("enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()