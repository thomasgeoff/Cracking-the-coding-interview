#1.String UNIQUE

def str_unique(str1):
#   if len(str1)>26:
#       return 'String is Unique' 
    c = 0
#    print(str1.lower())
    for i in str1.lower():
#        print("i:",i)
        if i.isalpha():
            for j in str1.lower():
#                print("j:",j)
                if i==j:
                    c+=1
#                    print("c:",c)
                if c>=2:
                    return 'String Not Unique'
            c=0
    return 'String is Unique'
    
print(str_unique('The qickk brwn fx jumps ov  lazy dg'))
print(str_unique('The quick brown fox jumps over the lazy dog'))
