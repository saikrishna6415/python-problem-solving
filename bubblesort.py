def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)