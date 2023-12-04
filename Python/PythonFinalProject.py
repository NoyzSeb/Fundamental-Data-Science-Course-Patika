import numpy as np
quest1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatQuest1=list()
quest2=[[1, 2], [3, 4], [5, 6, 7]]


def flatter(l):
    flatQuest1=list()
    for i in l:
        if type(i) == list:
            flatQuest1.extend(flatter(i))
        else:
            flatQuest1.append(i)
    return flatQuest1

def reverse_maker(l):
    l.reverse()
    for i in l:
        if type(i) == list:
            i.reverse()    
    return l

print(flatter(quest1))
print(reverse_maker(quest2))