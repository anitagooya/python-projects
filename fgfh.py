def solution(number):
    list = []
    list2 = []
    temp = 0
    while number != 10:
        list.append(number)
    for i in list:
        if i % 3==0 or i % 5==0:
            list2.append(i)
    for j in list2:
        temp = j + temp
    print(list)
    return temp
def main():
    print("salam")
    number = input("print a number ")
    print(solution(number))
if __name__ =="__main()__" :
    main()
