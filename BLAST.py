def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1
def Hits ():
    dic = {}
    f = open('C:\\Users\\Super Magic\\Desktop\\SEQ.txt', "r")
    seq = f.read()
    seeds = get_score()
    for j in seeds:
        for i in j:
            for n in range(len(seq)):
                if n + 11 > len(seq):
                    break
                if i == seq[n]:
                    if seq[n:n +11] == j:
                        dic[n] = j
    return dic
    #print(str(dic))
def extend ():
    f = open('C:\\Users\\Super Magic\\Desktop\\SEQ.txt', "r")
    seq = f.read()
    index = 0
    dichit = Hits()
    # threashold = 11
    #hspscore = get_score()
    Query = remove_repeat()
    words,neighbours = blastdna()
    for key ,value in dichit:
        start_db = key
        start_Q = index
        end_db = start_db + 11
        end_Q = start_Q + 11
        score = 0
        while True :
            if start_Q != 0:
                if Query[start_Q - 1] == seq[start_db - 1]:
                    score += 1
                    sequence += seq[start_db - 1]
            if Query[end_Q - 1] == seq[end_db - 1]:
                score += 1
                sequence += seq[end_db - 1]
            start_Q -=1
            start_db-=1
            end_db-=1
            end_Q-=1
            if end_db == len(seq) or end_Q != len(Query) :
                break
            if score < threashold :
                break
            else :
                score-=1
    print(sequence)           


def remove_repeat ():
    seq = "AAGCATGCCCATTCATTCACCGCTGCTACTGCATCTATTCATCTCATCTCATCGGGCATCCGTTAAACGGTCTCTGCTTCTCTATCTCTCAATTCTTACGATAGCGCTTTCTATCTCTATTCTGCGCGGCGCGCGCGCGCGTATCGCTTAGGTCATCTCATTGCCATGCAGTCAGTTCGCGCGCGCGCGCGCGCGCTAGCGGATCTCTTTAAATCTGCGTATCCAT"
    index = 0
    no_repeat = ""
    while True:
        if seq[index:index + 4] == "TTTT" or seq[index:index + 4] == "AAAA" or seq[index:index + 4] == "CCCC" or seq[
                                                                                                                 index:index + 4] == "GGGG":
            char = seq[index]
            while char == seq[index]:
                index += 1
        if seq[index] == 'C':
            if seq[index:index + 4] == "CGCG":
                index = index + 3
            else:
                no_repeat += seq[index]
        else:
            no_repeat += seq[index]
        index += 1
        if (index == len(seq)):
            break
    return no_repeat
def blastdna():
    words = []
    neigh = []
    z = []
    letters = ['A', 'C', 'G', 'T']
    sequery = remove_repeat()
    #print(sequery)

    for i in range(len(sequery)):
        ss = sequery[i:11 + i]
        if len(ss) == 11:
            words.append(ss)
    #print(words)

    for i in range(len(words)):
        for j in range(len(words[i])):
            for a in range(len(letters)):
                strr = list(words[i])
                strr[j] = letters[a]
                nn = listToString(strr)
                z.append(nn)
        neigh.append(z)
        z = []
    #print(neigh)
    return words,neigh
def get_score():
    words,neighbours = blastdna()
    threshold = 10
    neighdict = dict()
    hspneighbours = []
    for i in words:
        for j in neighbours:
            for neighb in j:
                score = 0
                for a,b in zip(neighb,i):
                    if a == b:
                        score += 1
                x = score
                if x > threshold:
                    neighdict[neighb] = x
    for key,value in neighdict.items():
        hspneighbours.append(key)

    return hspneighbours
get_score()
Hits()
