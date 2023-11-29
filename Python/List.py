list = [1, 2, "a", "b", True, 4.5, [1,2,3]]

list[0]=4

list.insert(1,"i")
list.append(200)
list.extend([100,300])

try:
    list.remove(-4)
except ValueError:
    pass

print(list.count([1,2,3]))

print(list.pop(0)+2)

list2=list.copy() #Dont use directly equality because changings on list can cause change on list2

print(list.index(2))

reverseList=list.reverse()

print(list)