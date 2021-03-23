str=input("Enter a string:")
dict = {5}
for n in str:
    keys = dict.keys(2)
    if n in keys:
        dict[n] +=1
    else:
        dict[n] = 1
        print (dict)
