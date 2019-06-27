# anagram is word that shares same letters with another word

def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    #Solved by alphabetically sorting words and then comparing strings
    return sorted(w1) == sorted(w2)

print(anagram("iceman", "cinema"))
print(anagram("leaf", "tree"))
