# Module MySorting.py

# 선택 정렬을 위한 selectionSort 함수 생성
def selectionSort(L):
    # 리스트의 사이즈를 구해 for문의 반복을 위한 size = len(L)
    size = len(L)
    for i in range(0, size-1):
        # 최솟값의 순서를 index_min으로 가정
        index_min = i
        for j in range(i+1, size):
            # 만약 L[j]가 이전에 구한 최솟값보다 작다면 최솟값의 순서를 j로 설정
            if (L[index_min] > L[j]):
                index_min = j
        if (index_min != i):
            L[i], L[index_min] = L[index_min], L[i]
    return L

# 병합정렬을 위한 merge,mergeSort 함수 생성


def _merge(L_left, L_right):

    L_res = []
    i, j = 0, 0

    len_left, len_right = len(L_left), len(L_right)

    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1

    while (i < len_left):
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res


def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = mergeSort(L[:middle])
        L_right = mergeSort(L[middle:])
        return _merge(L_left, L_right)
