words = []
while True:
    word = input()
    if word == "Stop":
        break
    elif word != "отмяна":
        words.append(word)
    elif word == "отмяна":
        words.pop()
print(words)