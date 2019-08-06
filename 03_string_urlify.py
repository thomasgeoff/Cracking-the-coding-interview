#3 String URLify

def str_urlify(str1):
    url = ''
    l = m = 0
    l=len(str1.split())
    for j in str1.split():
        m += len(j)
    print(l)
    print(m)
    c=0
    for i in str1:
        if i!=' ':            
            url+=i
        else:
            url+='%20'
        c+=1
        if c==(l+m-1):
            return url
        
print(str_urlify('The quick brown foxjumps over the lazydog                '))
