def remove_duplicates(array):
    
    if not array:
        return 0

    unik_count = 1

    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            unik_count += 1

    return unik_count

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4