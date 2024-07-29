lines=[]
orders=[]
receipt=[]
total=0.0
vat = 0.0

# Read menu.txt and store menu information in lines list
with open("menu.txt") as f:
    for line in f:
        line = line.rstrip().split(', ')
        line[2] = float(line[2]) # convert price to float
        line[3] = float(line[3]) # convert VAT percentage to float
        lines.append(line)

# Read ordine.txt and store order information in orders list
with open("ordine.txt") as file:
    for order in file:
        order = order.rstrip().split(', ')
        order[1] = float(order[1]) # convert quantity to float
        orders.append(order)

# Loop through both lines and orders lists to find matching items
for i in range(len(lines)):
    for j in range(len(orders)) :
        if lines[i][0] == orders[j][0]:
            item_total = lines[i][2] * orders[j][1]
            item_vat = item_total * (lines[i][3] / 100)
            receipt.append([lines[i][0], lines[i][2], orders[j][1], item_total, lines[i][3], item_vat])
            total += item_total
            vat += item_vat

# Sort the receipt list by item name
receipt.sort(key=lambda x:x[0])

# Output the generated receipt
print("RECEIPT")
for item in receipt:
    print(item[1], item[0], " ", item[2], "VAT", item[4], "%")
print("Total: ", total, "$")
print("VAT: ", vat, "$")