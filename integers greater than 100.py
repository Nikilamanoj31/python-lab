N = int(input(" Enter the total number of integers in the list: "))
list=[]
for i in range(N):
    num = input("Enter a number :")
    if int(num)>100:
        num="over"
    list.append(num)
print(list)
