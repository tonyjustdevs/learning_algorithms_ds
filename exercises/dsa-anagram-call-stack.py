import showcallstack as ss

def anagrams(string):
    ss.showcallstack()
    if len(string)==1:
        return string[0]
    collection = []
    substr_anagrams = anagrams(string[1:])
    for anagram in substr_anagrams:
        # ss.showcallstack()
        for i in range(len(anagram)+1):
            new_string = anagram[:i]+string[0]+anagram[i:]
            collection.append(new_string)
    return collection

anagrams("abc")