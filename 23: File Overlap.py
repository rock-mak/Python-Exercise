def happy():
    happyfile = open("happynumbers.txt")
    result = list(happyfile.read().split("\n"))
    return result
    
def prime():
    primefile = open("primenumbers.txt")
    result = list(primefile.read().split("\n"))
    return result
    
print([num for num in happy() if num in prime()])
