# import random number generator
from random import randrange
# import heap class
from Heap_Min import MinHeap

# make an instance of MinHeap
min_heap = MinHeap()

# set internal list for testing purposes...
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

print("The smaller child of index 1 is: ")
smaller_child_of_idx_1 = min_heap.get_smaller_child_idx(1)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_1]
print(smaller_child_element)

print("The smaller child of index 2 is: ")
smaller_child_of_idx_2 = min_heap.get_smaller_child_idx(2)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_2]
print(smaller_child_element)


print("The smaller child of index 3 is: ")
smaller_child_of_idx_3 = min_heap.get_smaller_child_idx(3)
smaller_child_element = min_heap.heap_list[smaller_child_of_idx_3]
print(smaller_child_element)
