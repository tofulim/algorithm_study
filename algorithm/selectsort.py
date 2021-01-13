#맨 왼쪽부터 하나씩 최소값을 선택(selection)해 채운다

def selection_sort(li):
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        if min_idx != i:
            li[i], li[min_idx] = li[min_idx], li[i]
    return li

if __name__ == "__main__":
    li = [4, 6, 1, 7, 2, 8, 3, 5, 9, 10, 12, 11]
    SelectionSort(li)
    print(li)