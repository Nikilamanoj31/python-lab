N=int(input("Enter the total number of elements in the list :"))
list=[]
for i in range(N):
    value=int(input("Enter the number :"))
    list.append(value)
for i in list :
    square=i**2
    print("The squaresof the number ",i," is:",square)        
