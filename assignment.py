#Q.1

a=int(input("Enter any no to check:"))

if a<0:
    print("The number is a Negative no:",a)
elif a>0:
    print("The number is a Positive no:",a)
else:
    print("The number is zero:",a)

#Q.2

a=int(input("Enter any no to check:"))

if (a%4==0 and a%100!=0) or a%400==0:
    print("The year is a leap year:",a)
else:
    print("The year is not a leap year:",a)

#Q.3

a=int(input("Enter any no to print its table:"))

for i in range(1,11):
    print(f"{a} x {i} = {a*i}")
print()

#Q.4

a=int(input("Enter any no to check no of digits:"))
dig=0

while a!=0:
    dig+=1
    a=a//10
print(f"The no of digits is:{dig}")


#Q.5

num=input('Enter the no to be reversed:')
print("Reversed no:",num[::-1])


#Q.6

a=int(input("Enter any no to calculate factorial:"))

fact=1
while a!=0:
    fact=fact*(a)
    a-=1
print(fact)

#Q.7

a=int(input("Enter any no to check for armstrong or not:"))
dig=0
temp=a
while temp!=0:
    dig+=1
    temp=temp//10

temp=a
total=0
while temp>0:
    rem=temp%10
    total=total+pow(rem,dig)
    temp=temp//10


if total==a:
    print("The no is armstrong:",a)
else:
    print("The no is not armstrong:",a)

#Q.8

#Skips multiple of 5
a=1

while a<21:
    if a%5!=0:
        print(a,sep=" ",end=" ")
        a+=1
    elif a%5==0:
        a+=1
    
#Stops when number reaches 16

a=1
print()
while a<17:
    
    print(a,sep=" ",end=" ")
    a+=1
    
#Q.9

num=input('Enter the no to be reversed:')
print('Given Number:',num)
rev=num[::-1]
print('Reverse:',rev)

if num==rev:
    print('The no is Palindrome')
else:
    print('The no is not Palindrome')

#Q.10

#Square star pattern


a="*"

for i in range(4):
    for j in range(4):
        print(a,sep=" ",end=" ")
    print()

#Square with gaps

a='*'

for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
            print(a,sep=" ",end=" ")
        else:
            print(" ",sep=" ",end=" ")
    print()

#pyramid

a=1

for i in range(5):
    print(" "*(4-i) + "*"*a)
    a+=2