def maxconrep(s):
    fin=s[0]
    n=len(s)
    maxcount=0
    
    for i in range(n):
        count=0
        
        for j in range(i,n):
            if(s[i]!=s[j]):
                break
            count+=1
            
        if (count>maxcount):
            maxcount=count
            fin=s[i]
            
    return fin
    
s=input("Enter a string:")
print(maxconrep(s))