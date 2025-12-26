#Q1

#Data strutures are ways of organising and storing data so that it can be accessed and modified efficiently.
#Data structures are vital because they help in organising data efficiently which helps in processing.

#Q2

l1=[11,4,17,8,21]
l1.append(12)
print(l1)
l1.insert(2,5)
print(l1)
l1.remove(l1[-1])
print(l1)
l1.sort()
print(l1)

#Q3

#list-list are ordered ,mutable data structures,it supports indexing and allows duplicates.
#tuple-tuple are ordered,immutable data structures,tuple are faster than list,also allows duplicates.

t1=(1,2,3)
print(t1[0])
t1[0]=8

#Q4

A={1,2,3,4,5}
B={3,4,6,7}

#Union

C=A|B
print(C)

#Intersection

D=A&B
print(D)

#Difference

E=A-B
print(E)

#Q5

l1=[11,4,17,8,4,21]
print(set(l1))

#Q6

a=input("Name;")
b=input("Roll No:")
c=int(input("Marks:"))
student={"Name:":a,"Roll No:":b,"Marks:":c}

student={"Name:":"Harsh","Roll No:":"13","Marks:":8.4}

for key,value in student.items():
    print(key,student[key])

#Adding Grade

print()

student["Grade:"]="A"
for key,value in student.items():
    print(key,student[key])

#Updating Marks

print()

student["Marks:"]=8.8
for key,value in student.items():
    print(key,student[key])

#Removing key

print()

del student["Roll No:"]
for key,value in student.items():
    print(key,student[key])

#Q7

#Dictionary are faster than list because:
#1:list elements are stored sequentially and python searches elements one by one-
#Time complexity of list:0(n)
#2:Dictionary elements are stored using hash value which points to memory location-
#Time complexity of list:0(1)


#Q8

text="Python Data Structures"

_low_text=text.lower()
print(_low_text)

_rep_text=text.replace("Data","Core")
print(_rep_text)

_spl_text=text.split()
print(_spl_text)

#Q9

for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
    else:
        print("",end=" ")

#Q10

#Storing fixed coordinates:tuple
#Storing unique email id's:set
#Storing user profile information:dictionary