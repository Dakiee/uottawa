def momo(st):
    length=len(st)
    a=st[0]
    count=0
    shineString=""
    for i in range(length):
        if(st[i]==a):
            count=count+1
        else:
            shineString+=a+str(count)
            a=st[i]
            count=1
    shineString+=a+str(count)
    return shineString

b=input("jo string ee oruulna uudaaa: ")
c=momo(b)
print(c)
