# fact=1
# i=int(input("Enter a number: "))
# for i in range(1,i+1):
#     fact=fact*i
# print("Factorial of",i,'is:',fact)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n=int(input('Enter a number: '))
print('factorial of',n,'is:',fact(n))    