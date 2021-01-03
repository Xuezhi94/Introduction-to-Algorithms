def insertion_sort(l):
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


l = [5,2,4,6,1,3]
insertion_sort(l)
print(l)
print(1)
 


