def voroodi ():
    adad = int(input(" 1 adad varad konid"))
    return adad

def binary (adad) :
    power2=[]
    binNew=[]
    n=0
    x=1
    while True :
        power2.append(2**n)
        n+=1
        if adad < 2**n:
            break
    for i in power2 :
        if adad - power2[-x] >= 0 :
            binNew.append(1)
            adad = adad - power2[-x]
            x+=1
        else:
            binNew.append(0)
            x+=1
    return binNew



def counter1 (list) :
    counter=0
    for i in list :
        if i ==1:
            counter+=1
    return counter





def main():
    print(binary(548))
    print(counter1(binary(548)))

if __name__=="__main__":
    main()