def main() :
    order_list = []
    menu_list = []
    reciept_item = []
    counter=0
    try:
        with open("menu.txt", "r") as menu_file:
            for item in menu_file.readline():
                product = item.rstrip().split(",")
                menu_list.append(product)
            print(menu_list)
    except:
        print("shit")
main()