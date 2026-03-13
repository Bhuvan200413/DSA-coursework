#counter problem approch
#count even no's From 1 to n
'''
def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            count +=1
    return count
def main():
    n =  int(input("Enter no: "))
    print("Even count: ", count_even(n))
main() '''

def count_n(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

def main():
    num = int(input("Enter a number: "))
    print("Count of digits:", count_n(num))
main()
