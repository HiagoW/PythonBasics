pos = -1

def search(list,number):
    
    for (n,i) in enumerate(list):
        if i == number:
            globals()['pos'] = n
            return True
    return False

list = [5,8,4,6,9,2]
n = 91

if search(list,n):
    print("Found at ", pos)
else:
    print("Not found")