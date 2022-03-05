def encrypt(word):
    hariu=""
    l=len(word)
    for i in range(0,l//2):
        hariu=hariu+word[l-1-i]+word[i]
    if(l%2==1):
        hariu=hariu+word[l//2]
    return hariu
        
        
        
print(encrypt("1234"))
print(encrypt("12"))
