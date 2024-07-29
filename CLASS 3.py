def strawberry_reader(filename) :
    raw=[]
    try:
        with open(filename) as strawberry:
            straw = strawberry.readlines()

    except OSError as error:
        print(error)
    for i in straw:
        temp = i.strip().split(' ')
        raw.append(temp)
    return raw

def core(list):
    list2=[]
    result=[]
    for line in list :
        for word in line:
            list2.append(word)
    print(list2)
    for i in range (len(list2)-2) :
        if len(list2[i])==len(list2[i+1]) and len(list2[i+1])==len(list2[i+2]) :
            result.append((list2[i], list2[i + 1], list2[i + 2]))
    print(result)
    return (result)

def main():
    print(core(strawberry_reader("strawberry-short.txt")))

if __name__ == "__main__":
    main()