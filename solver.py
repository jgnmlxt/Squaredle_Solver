from nltk.corpus import words
from nltk.corpus import wordnet
import numpy as np
puzzle=input("Please input the puzzle: ")
wordlist=[]
length_bt_three=[]
length_bt_three_steps=[]

def arrange(puzzle):
    puz=puzzle.split(",")
    pu=[]
    for p in puz:
        pu.append(list(p))

    print(pu)
    return pu

def isword(path,puzzle):
    word=""
    for i in path:
        word+=puzzle[i[0]][i[1]]

    if wordnet.synsets(word):
        if len(word)>3:
            length_bt_three.append(word)

        wordlist.append([word,path])


def search(node,path,used,neigh,ran):
    result=False
    x=node[0]
    y=node[1]
    temp=[]
    if x-1>=0 and x-1<ran[0] and y-1>=0 and y-1<ran[1] and (x-1,y-1) not in path and (x-1,y-1) not in used:
        temp.append((x-1,y-1))
        result=True
    if x-1>=0 and x-1<ran[0] and (x-1,y) not in path and (x-1,y) not in used:
        temp.append((x-1,y))
        result=True
    if x-1>=0 and x-1<ran[0] and y+1>=0 and y+1<ran[1] and (x-1,y+1) not in path and (x-1,y+1) not in used:
        temp.append((x-1,y+1))
        result=True
    if x>=0 and x<ran[0] and y-1>=0 and y-1<ran[1] and (x,y-1) not in path and (x,y-1) not in used:
        temp.append((x,y-1))
        result=True
    if x>=0 and x<ran[0] and y+1>=0 and y+1<ran[1] and (x,y+1) not in path and (x,y+1) not in used:
        temp.append((x,y+1))
        result=True
    if x+1>=0 and x+1<ran[0] and y-1>=0 and y-1<ran[1] and (x+1,y-1) not in path and (x+1,y-1) not in used:
        temp.append((x+1,y-1))
        result=True
    if x+1>=0 and x+1<ran[0] and (x+1,y) not in path and (x+1,y) not in used:
        temp.append((x+1,y))
        result=True
    if x+1>=0 and x+1<ran[0] and y+1>=0 and y+1<ran[1] and (x+1,y+1) not in path and (x+1,y+1) not in used:
        temp.append((x+1,y+1))
        result=True
    if result==True:
        neigh.append(temp)
    return neigh, result

puzzle=arrange(puzzle)
ran=(len(puzzle),len(puzzle[0]))
for x in range(ran[0]):
    for y in range(ran[1]):
        path=[(x,y)]
        used=[]
        neigh=[]
        
        neigh,result=search(path[-1],path,used,neigh,ran)
        print("now is",x,y)

        while(len(neigh)!=0):
            path.append(neigh[-1][-1])
            isword(path,puzzle)
            neigh,result=search(path[-1],path,used,neigh,ran)
            if result == False:
                neigh[-1]=neigh[-1][:-1]
                path=path[:-1]
            while len(neigh)!=0 and len(neigh[-1])==0:
                neigh=neigh[:-1]
                path=path[:-1]
                if len(neigh)!=0:
                    neigh[-1]=neigh[-1][:-1]
            
        if len(neigh)==0:
            continue
                
print(np.unique(length_bt_three))
