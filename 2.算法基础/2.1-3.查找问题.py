#问题描述：
#   输入：n个数的一个数列A和一个值v
#   输出：下标 i 使得 v=A[i]，或者v不在A中，v为特殊值Nul(返回None)
def search(l,v):
    for i in range(len(l)):
        if v == l[i]:
            return i
    print('v为特殊值Nul')
    return None

l = [1,2,3,4,5,6]
print(search(l,3))
print(search(l,9))
