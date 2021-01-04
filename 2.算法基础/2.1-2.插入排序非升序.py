def insertion_sort_dec(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key > l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key

l = [4,5,7,3,2,9,7]
insertion_sort_dec(l)
print(l)
