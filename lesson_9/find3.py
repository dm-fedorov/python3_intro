# find3.py
def find_two_smallest(L):
    if L[0] < L[1]:           
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    for i in range(2, len (L)):
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
            min2 = i
    return (min1, min2)

if __name__ == "__main__":
    print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324,  476]))    
