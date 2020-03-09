class DynamicArray:
#my_array = [4] #make an empty array of size 4,NOT a 1 size array with a 4
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
    
    #make sure we have open space
        if self.count >= self.capacity:
        #TODO: make array dynamically resize
            self.double_size()
            # print("ERROR :Array is full")
            return

    #make sure index in range
        if index > self.count:
            print("Error: Index out of range")


    #shift everything over to the right
    #start with the last one, move it ot the right
    #strting, stopping, iterative
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]


    #insert our value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *=2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            #new storage becomes old storage
            new_storage[i] = self.storage[i]

        self.storage=new_storage

my_array = DynamicArray(4)
my_array.insert(0, 1)
my_array.insert(0,2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)
my_array.append(20)

print(my_array.storage)

#[2,3,1,4]

#after adding double capacity
