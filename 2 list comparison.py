list1=[2,5,7,9,4]
list2=[7,9,10,5,6]
print("The first list is:",list1)
print("The second list is:",list2)
if len(list1)==len(list2):
    print("Both lists have same length.")
else:
    print("length are not same.")
print("Sum of elements in list1:",sum(list1))
print("Sum of elements in list2:",sum(list2))
if sum(list1)==sum(list2):
    print("The sum of the lists are same.")
else:
    print("The sum of the lists are not same.")
    list3=[]
    list3=[each for each in list1 if each in list2]
print("The commom values in the lists are:",list3)
