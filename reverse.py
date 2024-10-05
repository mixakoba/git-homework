def shemotrialebuli(str1):
    if not isinstance(str1,str):
        return print("sheiyvanet stringi")
    left,right=0,len(str1)-1
    shemotrialebuli_str=list(str1)
    while left<=right:
        shemotrialebuli_str[left],shemotrialebuli_str[right]=shemotrialebuli_str[right],shemotrialebuli_str[left]
        left+=1
        right-=1
    return "".join(shemotrialebuli_str)
print(shemotrialebuli("abc"))