def main():
    menu_list = []
    orders_list = []
    receipt_items = []
    counter = 0
    total = 0
    vat_total = 0
    try:
        with open("menu.txt", "r") as menu_fl:
            for item in menu_fl.readlines():
                product = item.rstrip().split(", ")
                product[2] = float(product[2])
                product[3] = float(product[3])
                menu_list.append(product)
        # print(menu_list)
    except Exception as e:
        print(e)
    try:
        with open("ordine.txt", "r") as ordine_fl:
            for item in ordine_fl.readlines():
                order = item.rstrip().split(", ")
                order[1] = int(order[1])
                orders_list.append(order)
        # print(orders_list)

    except Exception as e:
        print(e)


    for order in orders_list:
        order_a = list(filter(lambda x: x[0] == order[0], menu_list))
        order_a[0].append(order[1])
        receipt_items.extend(order_a)
    #print(receipt_items)
    receipt_items.sort(key= lambda x: x[3])
    #print(receipt_items)


    print("RECEIPT")
    for item in receipt_items:
        sum_item = (item[2] * item[4])
        print(item[4], item[1], " "*(26-len(item[1])), sum_item, "VAT", f"{item[3]}%")
        total = total + sum_item
        vat_item = (item[3])/100
        total_vat_item = sum_item * vat_item
        vat_total = vat_total + total_vat_item


    print("Total: ", total,"$") # Sorry, I didn't find the Euro sign :(
    print("VAT: ", round(vat_total,2),"$")
main()