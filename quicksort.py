import time
import random


def quickSort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        #sort both halves
        quickSort(myList, start, pivot - 1)
        quickSort(myList, pivot + 1, end)
    return myList


def partition(myList, start, end):
    pivot = myList[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            #swap places
            temp = myList[left]
            myList[left] = myList[right]
            myList[right] = temp

    #swap start with myList[right]~
    temp = myList[start]
    myList[start] = myList[right]
    myList[right] = temp
    return right


if __name__ == '__main__':
    List = []
    for i in range (20):
        List.append(random.randrange(1, 666, 1))
        print(List)
    start = time.time()
    print('Sorted List:', quickSort(List, 0, len(List) - 1))
    stop = time.time()
    print('Time Required: ', (stop - start))
