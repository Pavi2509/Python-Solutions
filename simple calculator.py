print("Select the operation to be performed")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
choice=input("Enter your choice : ")
choice=int(choice)
a=input("Enter the first number : ")
b=input("Enter the second number : ")
if choice == 1:
    sum=int(a)+int(b)
    print("Sum = "+str(sum))
elif choice==2:
    diff=int(a)-int(b)
    print("Difference = "+str(diff))
elif choice==3:
    pr=int(a)*int(b)
    print("Product = "+str(pr))
elif choice==4:
    div=int(a)/int(b)
    print("Division = "+str(div))
elif choice==5:
    po=int(a)**int(b)
    print("Power = "+str(po))
else:
    print("Invalid Choice")
