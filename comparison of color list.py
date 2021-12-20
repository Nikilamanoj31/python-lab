A=int(input("Enter the number of colors in the list-1:"))
color_list1=[]
for i in range(A):
    value=input("Enter color:")
    color_list1.append(value)
B=int(input("Enter the number of colors in the list-2:"))
color_list2=[]
for i in range(B):
    value=input("Enter color:")
    color_list2.append(value)
color_list3=[]
color_list3=[each for each in color_list1 if each in color_list2]
print("The colors from color-list1 not contained in color-list2:",color_list3)
