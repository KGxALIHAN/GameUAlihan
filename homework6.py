def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# пример использования
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
def binary_search_block(arr, val):
    N = len(arr)
    result_ok = False
    first = 0
    last = N - 1
    pos = -1
    
    while first <= last and not result_ok:
        middle = (first + last) // 2  # Делим индекс пополам
        
        if arr[middle] == val:
            result_ok = True
            pos = middle
        elif val > arr[middle]:
            first = middle + 1
        else:
            last = middle - 1
    
    if result_ok:
        print(f"Элемент {val} найден на индексе {pos}.")
    else:
        print(f"Элемент {val} не найден в списке.")
    
# Пример использования
sorted_list = [11, 12, 22, 25, 64]
target_element = 22
binary_search_block(sorted_list, target_element)
