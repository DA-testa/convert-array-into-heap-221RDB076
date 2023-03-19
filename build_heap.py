#python3

def sift_down(i, arr, swaps):
    min_index = i
    left_child = 2*i + 1
    right_child = 2*i + 2
    n = len(arr)
    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child
    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(min_index, arr, swaps)

def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(i, arr, swaps)
    return swaps

if __name__ == '__main__':
    menu = input()
    if(menu == "I"):
        n = int(input())
        print(n)
        arr = list(map(int, input().split()))
        swaps = build_heap(arr)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    elif(menu =="F"):
         f = open(input(), "r", -1, "UTF-8")
         print(f.read())
        
