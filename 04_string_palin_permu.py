#4.String Palindrome Permution
def str_permutation(str1):
    count = {}
    for i in str1.lower():
        if i.isalpha():
            count[i] = count.get(i, 0) + 1
    print(count) 
    odd=0
    for value in count.values():
        if value%2!=0:
            odd+=1
    print("oddcount:",odd)
    if odd > 1:
        print("1:Strings does not satisfies palindrome permutation")
    else:
        print("2:Strings satisfies palindrome permutation")
            

str_permutation('Tact Coa') #True
str_permutation('jhsabckuj ahjsbckj') #True
str_permutation('Able was I ere I saw Elba') #True
str_permutation('So patient a nurse to nurse a patient so') #False
str_permutation('Random Words') #False
str_permutation('Not a Palindrome') #False
str_permutation('no x in nixon') #True
str_permutation('azAZ') #True
