#  冒泡排序

def BubbleSort(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print(a)

a = [5, 6, 8, 4, 3, 7, 10, 2]
BubbleSort(a)