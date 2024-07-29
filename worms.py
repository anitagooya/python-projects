def seqtxt_reader(filename):
    bigList=[]
    try :
        with open(filename) as sequence :
            for line in sequence:
                word=line.rstrip().split(" ")
                 # for word in line:
                bigList.append(word)
    except OSError as error:
        print(error)


    return bigList
def voorodi() :
    word1=str(input("print a word"))
    word2=str(input("print second word"))
    return word1, word2
def core(bigList, word1, word2):
    temp = []
    temp2 = []
    counter = 0
    counter2= 0
    adad=[]
    seq_ind = []
    counter_jomalat = 0
    for i in bigList:
        seq_ind.append(counter_jomalat)
        for j in i:
            counter_jomalat +=1
        seq_ind.append(counter_jomalat-1)

    for word in bigList :
        for i in word:
            if i == word1:
                temp.append(counter)
            counter += 1
        for j in word:
            if j ==  word2:
                temp2.append(counter2)
            counter2 += 1
    for t in temp:
        for u in temp2:
            javab= u-t
            if javab>=0:
                adad.append(javab)
    print(temp, temp2, adad)
    print(seq_ind)
    # for javab in adad:
    #     jaVAB =min(o)
    # print(jaVAB)

    return temp,temp2

def main():
    #word1,word2 = voorodi()
    print(seqtxt_reader("seq.txt"))
    biglist = seqtxt_reader("seq.txt")
    inx1,inx2 = core(biglist,"time","line")


if __name__ =="__main__" :
    main()