def merge(left, right, data):
    nL = len(left)
    nR = len(right)
    i = 0
    j = 0
    k = 0
    while i < nL and j < nR:
        if left[i] < right[j]:
            left[i] = data[k]
            i += 1
        else:
            right[j] = data[k]
            j += 1
        k += 1
    while i < nL:
        left[i] = data[k]
        i += 1
        k += 1
    while j < nR:
        right[j] = data[k]
        j += 1
        k += 1
    return data


def mergesort(data):
    n = len(data)
    if n < 2: return
    mid = n // 2
    left = []
    right = []
    for i in range(0, mid):
        left.append(data[i])
    for j in range(mid, n):
        right.append(data[j])
    merge(left, right, data)
    mergesort(left)
    mergesort(right)
    return data


A = [9, 6, 3, 1, 7, 5, 8, 4]
print(mergesort(A))
