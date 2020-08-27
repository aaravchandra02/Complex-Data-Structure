class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    # END OF HEAP HELPER METHODS

    # define .retrieve_min() below...
    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[1]
        print("Removing: {min} from {self.heap_list}")
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        print(f"Last element moved to first: {self.heap_list}")

        # adding heapify down call
        self.heapify_down()
        return min

    # added this function
    def heapify_down(self):
        print("Heapifying down!")
        idx = 1

    # added this function
    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)  # return left child index
        else:
            # return left_child value
            left_child = self.heap_list[self.left_child_idx(idx)]
            # return right_child value
            right_child = self.heap_list[self.right_child_idx(idx)]

            # Checking which of the two child nodes are greater.
            if(left_child < right_child):
                print("left is greater\n")
                return self.left_child_idx(idx)
            else:
                print("right is greater\n")
                return self.right_child_idx(idx)

    def add(self, element):
        self.count += 1
        print("Adding: {element} to {self.heap_list}")
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                print("swapping {tmp} with {self.heap_list[idx]}")
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)
        print("HEAP RESTORED! {self.heap_list}")
        print("")
