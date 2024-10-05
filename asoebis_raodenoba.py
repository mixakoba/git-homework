def raodenoba(str1):
    if not isinstance(str1,str):
        return print("sheiyvanet stringi")
    x=dict()
    for i in str1:
        if i not in x:
            x[i]=1
        else:
            x[i]+=1
    return x

print(raodenoba("hello"))