
def missed_letters(text: str) -> str:
    missed = [None]*26
    for letter in range(ord("a"), ord("z")+1):
        missed[letter - ord("a")] = True
    

    for el in text:
  
        if ord(el) >= ord("a") and ord(el) <= ord("z"):
            missed[ord(el) - ord("a")] = False
        
    result = ""
    for i in range(len(missed)):
        if missed[i] == True:
            result += chr(i + ord("a"))

    return result

