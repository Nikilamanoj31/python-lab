element=input("Enter a statement:")
vowels=['a','e','i','o','u']
list=[]
for x in element:
    if(x in vowels and x not in list):
        
        print("vowels present in given statement:",x)
