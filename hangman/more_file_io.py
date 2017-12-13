import os
import random

path = "Puzzles"

file_names = os.listdir(path)

for i, f in enumerate(file_names):
    print(str(i) + ") " + f)

choice = input('pick one ')
choice = int(choice)

file = path + "/" + file_names[choice]
print(file)

with open(file, 'r') as f:
          lines = f.read().splitlines()

print(lines)

category_name = lines[0]
puzzle = random.choice( lines[1:])

print(category_name)
print(puzzle)
