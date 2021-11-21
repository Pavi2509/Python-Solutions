#using different methods in list
n=int(input("Enter the size of list 1 : "))
print("Enter the contents of list 1")
l1=[]
for i in range(int(n)):
    x=input()
    l1.append(x) 
print("appending all contents to list l1:")
print(l1)
l=[int(i) for i in input("Enter the contents of list 2 : ").split()]
l2=l.copy() 
print("copying contents of list l to list l1 : ")
print(l2)
print("using clear method to clear list l : ")
l.clear()
print(l)
print("join list l1 and l2 : ")
l1=l1.extend(l2)
print(l1)
print("Sorted list : ")   
print(l1.sort())
print("reversing list : ")
r=s.reverse()
print(r)


