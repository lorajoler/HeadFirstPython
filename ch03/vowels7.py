vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")

word_set = set(list(word))
found = word_set.intersection(set(vowels))

for vowel in found:
    print(vowel)
    
