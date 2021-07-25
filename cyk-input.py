word = input("Gib das Wort ein\n")

G = ""
while(True):
    text = input("Gebe eine neue Produktion der Form \"S AB BC\" für (S -> AB | BC) ein:\n")
    if(text == "NONE"):
        break
    text = text.split(" ")
    states = text[1]
    for i in range(2, len(text)):
        states += " | "+str(text[i])
    G += str(text[0]+" -> "+states+"\n")

def inputToGrammar(inp):
    res = {}
    for line in inp.split("\n"):
        if line == "\n":
            continue
        line = line.replace(" ", "")
        splitted = line.split("->")
        if len(splitted) < 2:
            continue
        v = splitted[0]
        right = splitted[1]
        res[v] = []
        for possibility in right.split("|"):
            res[v].append(possibility)
    return res

def printer(word, table):
    space = 30
    print("CYK".ljust(space) + "|  ", end = "")
    for i in range(len(word)):
        print(str(i+1).ljust(space), end = "")
    print()
    print("-"*((len(word)+1)*space+2))
    for i in range(len(word)):
        print((str(i+1)+ ": "+ word[i]).ljust(space) + "|  ", end="")
        for j in range(len(word)):
            if i + j <= len(word)-1:
                string = table[i][j].__repr__()
                if string == "set()":
                    print("{}".ljust(space), end = "")
                else:
                    print(string.ljust(space), end = "")
            else:
                print(" "*space, end = "")
        print()

from itertools import product

G2 = inputToGrammar(G)
table = [[set() for _ in range(len(word))] for __ in range(len(word))]

for length in range(1, len(word)+1):
    for i in range(len(word)-length+1):
        searches = []
        if length == 1:
            searches.append(word[i])
        else:
            for newLength in range(1, length):
                v1 = table[i][newLength-1]
                v2 = table[i+newLength][length-newLength-1]

                searches += [''.join(i) for i in product(*[v1, v2])]

        for k, v in G2.items(): 
            for res in v:
                for s in searches:
                    if s == res:
                        table[i][length-1].add(k)

printer(word, table)
input("Press Enter to exit")
