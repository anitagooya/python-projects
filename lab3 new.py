lines=[]
orders=[]
receipt=[]
total=0.0
with open("menu.txt") as f:
    lines=f.readline()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip().split(", ")
print(lines)