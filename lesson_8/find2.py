# find2.py
def find_two_smallest(L):
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    return (min1, min2)

if __name__ == "__main__":
    print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))    
