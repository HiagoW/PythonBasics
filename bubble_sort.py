def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if (list[j+1] < list[j]):
                lower = list[j+1]
                list[j+1] = list[j]
                list[j] = lower

list = [5,3,8,6,7,2]

sort(list)

print(list)