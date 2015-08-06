__author__ = 'Ruslan'
import random, math


def swap(array, l1, l2):
    tmp = array[l1]
    array[l1] = array[l2]
    array[l2] = tmp


def partition(array, l, r, pivot_ind):
    pivot_value = array[pivot_ind]
    array[pivot_ind] = array[r]
    array[r] = pivot_value
    ind = l
    for i in range(l, r):
        if array[i] < pivot_value:
            tmp = array[i]
            array[i] = array[ind]
            array[ind] = tmp
            ind += 1
    array[r] = array[ind]
    array[ind] = pivot_value
    return ind


def quicksort_recursive(array, l, r):
    if l >= r:
        return
    pivot_ind = math.floor(random.random()*(r-l+1)) + l
    p = partition(array, l, r, pivot_ind)
    quicksort_recursive(array, l, p-1)
    quicksort_recursive(array, p+1, r)


def quicksort_iterative(array, l, r):
    stack = [l, r]
    while len(stack) > 0:
        r = stack.pop()
        l = stack.pop()
        pivot_ind = math.floor(random.random()*(r-l+1)) + l
        p = partition(array, l, r, pivot_ind)
        if p-1 > l:
            stack.append(l)
            stack.append(p-1)
        if p+1 < r:
            stack.append(p+1)
            stack.append(r)


def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    copy_left = array[left:mid+1]
    copy_right = array[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while (i < n1) & (j < n2):
        if copy_left[i] < copy_right[j]:
            array[k] = copy_left[i]
            i += 1
        else:
            array[k] = copy_right[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = copy_left[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = copy_left[j]
        j += 1
        k += 1


def mergesort_iterative(array):
    n = len(array)
    for size in range(1, n):
        for left in range(0, n, 2*size):
            mid = left + size - 1
            if mid < n:
                right = min(left + 2*size - 1, n-1)
                merge(array, left, mid, right)