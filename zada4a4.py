words = list(input())
reversed = []
for i in range(len(words)):
    reversed.append(words.pop())
print("".join(reversed))