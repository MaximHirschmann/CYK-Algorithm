word = "baaba"

G = """

S -> AB | BC
A -> BA | a
B -> CC | b
C -> AB | a

"""


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
                l1 = word[i:i+newLength]
                l2 = word[i+newLength:i+length]

                v1 = table[i][newLength-1]
                v2 = table[i+newLength][length-newLength-1]

                searches += [''.join(i) for i in product(*[v1, v2])]

        for k, v in G2.items(): 
            for res in v:
                for s in searches:
                    if s == res:
                        table[i][length-1].add(k)

printer(word, table)