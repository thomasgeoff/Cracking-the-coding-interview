#2.String Permution
def str_permutation(str1,str2):
    if " " in str1 or " " in str2:
        print("One or both strings contains 'blank_space' in them")
        return
    if len(str1)!=len(str2):
        print("1:Strings does not satisfies permutation")
    else:
        c=0
        for i in str1:
            if i in str2:
                c+=1
        if c==len(str1):
            print("2:Strings satisfies permutation")
        else:
            print("2:Strings does not satisfies permutation")
            
str_permutation('ogd','god')
str_permutation('Godd','god')
str_permutation('God','god')
str_permutation('dgo  ','god')
