lines=[]
orders=[]
receipt=[]
total=0.0
with open("menu.txt") as f:
    for line in f:
        line = line.rstrip().split(', ')
        for e in range(len(lines)):
            lines[e][2]=float(lines[e][2])
            lines[e][3]=float(lines[e][3])
        lines.append(line)
with open("ordine.txt") as file:
    for order in file:
        order=order.rstrip().split(', ')
        for z in range(len(orders)):
            orders[z][1]=float(orders[z][1])
        orders.append(order)
for i in range(len(lines)):
    for j in range(len(orders)) :
        if lines[i][0]==orders[j][0]:
            receipt.append(lines[i])

            #for p in range(len(receipt)):
              #  total = total + (receipt[p][2]) * (orders[j][1])
#for e in range(len(receipt)):
 #   float(receipt[e][3]) and float(receipt[e][4])
#for s in range(len(receipt)):
 #   receipt.sort(key=lambda x:x[4])
print("receipt")
for item in receipt:
    for j in range(len(orders)):
       print(orders[j][1],item[1], item[2], item[3])