def word_count(str):
    counts = {}
    words = str.split()

    for word in words:
        if word in counts:
            print(word)
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
lie = "the word over here"
print([*lie])
letter_list = []
for letter in lie:
    letter_list.append(letter)
print(letter_list)
print()
e = {}
for letter in letter_list:
    if letter in e:
        e[letter] += 1
    else:
        e[letter] = 1
print(e)
