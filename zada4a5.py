from collections import deque
line = deque()
len_line = int(input("how many people are in the line:"))
for i in range(len_line):
    names = input("names ")
    line.append(names)
while line:
    print(f"обслужен: {line.popleft()} ")
