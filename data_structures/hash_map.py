import binascii
import sys


def get16bits(data):
    """Returns the first 16bits of a string"""
    # return int(binascii.hexlify(data), 16)
    return int.from_bytes(data.encode(), 'big')


class HashNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap(object):
    def __init__(self, default_size=10, table_threshold=0.7):
        self.table = [None] * default_size
        self.size = 0
        self.table_threshold = table_threshold

    def add(self, key, value):
        self.add_to_table(key, value)
        self.increase_table_size()

    def get(self, key):
        hash_idx = self.hash_function(key)

        node = self.table[hash_idx]

        while node is not None:
            if node.key == key:
                return node

        return None

    def add_to_table(self, key, value):
        hash_idx = self.hash_function(key)

        head = self.table[hash_idx]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.table[hash_idx]
        newNode = HashNode(key, value)
        if head is not None:
            newNode.next = head

        self.table[hash_idx] = newNode
        self.size += 1

    def increase_table_size(self):
        if (self.size * 1.0) / len(self.table) >= self.table_threshold:
            temp = list(self.table)
            self.size = 0
            self.table = [None] * len(self.table) * 2
            for node in temp:
                while node is not None:
                    self.add(node.key, node.value)
                    node = node.next

    """
        This is a light weight hash function
        For a robust hash function, please consider Paul Hsieh hash function

        Paul Hsieh is discussed at http://www.azillionmonkeys.com/qed/hash.html
        A Python is available at https://github.com/JRBANCEL/PySuperFastHash/blob/master/SuperFastHash.py
    """
    def hash_function(self, data):
        hash = len(self.table)  # gets the current length of the table
        b16_data = get16bits(data)  # converts a string to int representation
        return b16_data % hash

# s = HashMap(default_size=10)
# s.add("01", 1)
# s.add("02", 1)
# s.add("03", 1)
# s.add("04", 1)
# s.add("11", 1)
# s.add("22", 1)
# s.add("31", 1)
# s.add("41", 1)
# s.add("11", 1)
# s.add("21", 1)
# s.add("31", 1)
