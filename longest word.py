N=int(input("enter the number of words:"))
a=[]
for i in range(N):
    s=input("Enter element:")
    a.append(len(s))
print("length of longest word is",max(a))
