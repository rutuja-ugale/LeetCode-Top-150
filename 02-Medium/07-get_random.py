import random
class RandomizedSet:
    def __init__(self):
        # maps value to its index in self.nums
        self.val_to_idx = {}
        # stores the actual values for 0(1) random access
        self.nums = []
    def insert(self, val):
        if val in self.val_to_idx:
            return False
        # add to hash map and list
        self.val_to_idx[val] = len(self.nums)
        self.nums.append(val)
        return True
    def remove(self, val):
        if val not in self.val_to_idx:
            return False
        # identify the element to remove and the last element in the list
        idx_to_remove = self.val_to_idx[val]
        last_val = self.nums[-1]
        # move the last element to the spot of the element we want to remove
        self.nums[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove
        # remove the last element from the list and delete from map
        self.nums.pop()
        del self.val_to_idx[val]
        return True
    def getRandom(self):
        return random.choice(self.nums)