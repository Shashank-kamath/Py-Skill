def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_index = i
        
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]


input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()]


selection_sort(input_list)


print("Sorted list:", input_list)
