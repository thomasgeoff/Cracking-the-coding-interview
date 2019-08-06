def str_one_edit(str1,str2):
    if str1==str2:
        return  True
    l1 = len(str1)
    l2 = len(str2)
    c = 0
    if abs(l1-l2)>1:
        return  False
    st=st1=''
    if l1>=l2:
        st = str1
        st1 = str2
    else:
        st1 = str1
        st = str2
    for i in st:
        if i in st1:
            c+=1
#    print("str1: {}   str2: {}  c: {} l1:{} l2:{}".format(str1,str2,c,l1,l2))
    if abs(c-len(st))<=1:
        return True
    else:
        return False

data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]    
        
for k in range(0,len(data)):
    print(str_one_edit(data[k][0],data[k][1]))
