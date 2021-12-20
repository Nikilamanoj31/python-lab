N=int(input("Enter the total number of elements in dictionary :"))
dic={}
for i in range(N):
    dic[i]=input("Enter element:")
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0])))
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
