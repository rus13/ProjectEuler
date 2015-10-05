__author__ = 'Ruslan'
import random, math


def swap(array, l1, l2):
    array[l1], array[l2] = array[l2], array[l1]


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
    copy_left = array[left:mid]
    copy_right = array[mid:right]
    i = 0
    j = 0
    k = left
    while (i  < len(copy_left)) & (j  < len(copy_right)):
        if copy_left[i] < copy_right[j]:
            array[k] = copy_left[i]
            i += 1
        else:
            array[k] = copy_right[j]
            j += 1
        k += 1
    while i < len(copy_left):
        array[k] = copy_left[i]
        i += 1
        k += 1
    while j < len(copy_right):
        array[k] = copy_right[j]
        j += 1
        k += 1


def mergesort_iterative(array, l, r):
    n = len(array)
    size = 1
    while size < n:
        for left in range(l, r - size, 2*size):
            mid = left + size
            right = min(left + 2*size, n)
            merge(array, left, mid, right)
        size *= 2


def mergesort_recursive(array, l, r):
    if l + 1 >= r:
        return
    mid = (l+r)//2
    mergesort_recursive(array, l, mid)
    mergesort_recursive(array, mid, r)
    merge(array,l,mid,r)