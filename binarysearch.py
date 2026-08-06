# Binary Search

arr = [10, 20, 30, 40, 50]
key = 40

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found")
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if low > high:
    print("Element not found")