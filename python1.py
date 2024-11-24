def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        else:
            result+=chr((ord(char)+s-97)%26+97)
    return result
def decrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)-s-65)%26+65)
        else:
            result+=chr((ord(char)-s-97)%26+97)
    return result
text="ATTACK"
s=4
print("text:"+text)
print("shift:"+str(s))
encryptword=encrypt(text,s)
print("cipher:"+encryptword)
decryptword=decrypt(encryptword,s)
print("plaintext:"+decryptword)
            
