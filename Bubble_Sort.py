
lst = [8,1,5,3,2,0]



def Bubble_Sort(list):
    for j in range(len(list)-1):
        for i in range(0,len(list) - 1 - j):
            if(list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
    return list






Bubble_Sort(lst)
print(lst)











