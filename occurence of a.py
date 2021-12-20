N=int(input("Enter the number of names in the list : "))
list = []
count=0
for i in range(N):
    name = input("Enter name : ")
    list.append(name)
for i in list:
    for j in i:
        if(j=="a"):
            count=count+1;
print("Occurence of 'a' within the list :",count)
