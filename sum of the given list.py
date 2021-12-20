N=int(input("Enter the number of elements in the list:"))
list=[]
for i in range(N):
    value=int(input("enter the item:"))
    list.append(value)
sum_list=sum(list)
print("The sum of the items in the given list:",sum_list)
