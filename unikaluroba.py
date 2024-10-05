def unikaluri(str1):
    if not isinstance(str1,str):
        return print("sheiyvanet string tipis monacemi")
    x=set()

    for y in str1:
        if y in x:
            return False
        x.add(y)
    
    return True
print(unikaluri("abc"))
print(unikaluri("abb"))