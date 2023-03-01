pos = -1

def search(list,number):
    
    upper = len(list)-1
    lower = 0

    while upper >= lower:
        mid = (upper+lower) // 2
        if(list[mid] == number):
            globals()['pos'] = mid
            return True
        elif list[mid] > number:
            upper = mid-1
        else:
            lower = mid+1
    return False

list = [1,2,6,9,10,13,15,22,29,35]
n = 22

if search(list,n):
    print("Found at ", pos)
else:
    print("Not found")