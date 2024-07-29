menu_list = []
with open("menu.txt", "r") as menu_fl:
        for item in menu_fl.readlines():
            product = item.rstrip().split(", ")
            product[2] = float(product[2])
            product[3] = float(product[3])
            menu_list.append(product)
print(menu_list[0])
