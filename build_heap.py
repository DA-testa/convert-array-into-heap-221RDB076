#python3

globcnt = 0

def sift_down(i, arr, swaps):
    global globcnt
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
        globcnt = globcnt  +1
        sift_down(min_index, arr, swaps)

def build_heap(arr):
    global globcnt
    globcnt = 0
    n = len(arr)
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(i, arr, swaps)
    return swaps

if __name__ == '__main__':
    menu = input().strip('\r').strip('\n')
    if(menu == "I"):
        n = int(input())
        arr = list(map(int, input().split()))
        swaps = build_heap(arr)
        print(globcnt)
        for i, j in swaps:
            print(i, j)
        #print("Kapec tests norauj beigas ar trim un pec tam sudzas ka nav enter A0???????")
        #if (len(swaps) > 0):
        #    print(" \n", end="")
    elif(menu =="F"):
    #print 3. testu var apiet ja vienkrši izdruka visu faila saturu.
         f = open("tests/"+input(), "r", -1, "UTF-8")
         arr = list(map(int, f.read().split()))
         swaps = build_heap(arr)
        print(globcnt)
        for i, j in swaps:
            print(i, j)         
         #print(f.read())
        
