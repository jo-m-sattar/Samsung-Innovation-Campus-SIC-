
words = []


print("Enter 5 words:")
words.append(input("Word 1: "))
words.append(input("Word 2: "))
words.append(input("Word 3: "))
words.append(input("Word 4: "))
words.append(input("Word 5: "))


shortest_length = len(words[0])
for word in words:
    if len(word) < shortest_length:
        shortest_length = len(word)


print("Shortest word(s):")

for word in words:
    if len(word) == shortest_length:
        print(word)
