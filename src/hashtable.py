# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        
    #take key and turn it into an index in array 
        index = self._hash_mod(key)
        

    #check if something already at the index
        if self.storage[index] is not None:

     #make new linked pair
            LP= LinkedPair(key, value)

    #set new to existing
            LP.next = self.storage[index]
            
    #update index
            self.storage[index] = LP

    #else nothing was there so put it there
        else:
    # setting value at index to linked pair with they key and value
            self.storage[index] = LinkedPair(key, value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        #index
        index = self._hash_mod(key)

  # Print a warning if the key is not found
        if self.storage[index] is None:
            print("Error: key not found")
        else:

       #index reassigned to none
            self.storage[index] =None
            

        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        #index
        index = self._hash_mod(key)

        #if something at index
        if self.storage[index] is not None:
            #set current to index
            current = self.storage[index]
            #while not none
            while True:
        #if key matches
                if current.key == key:
        #Retrieve the value stored with the given key.
                    return current.value
        #At the end of storage
                elif current.next != None:
        #set current to next
                    current=current.next
                else:
                    return None
                    
        #key does not match anything        
        else:
                print("Error: key does not match")

                return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.v 
        '''
        #set current to old
        old_storage = self.storage
        self.capacity *=2
        self.storage = [None] * self.capacity

#loop through old storage
        for bucket_item in old_storage:
            #if bucket_item not none
            if bucket_item is not None:
             
                    #add key value
                    self.insert(bucket_item.key, bucket_item.value)
                    #set current to next bucket_item
                    

        #     #new index rehashed
        #         new_index = self._hash_mod(new_item.key)
        #     #newstorage = LinkedPair
        #         new_storage[new_index] = LinkedPair(new_item.key, new_item.value)

        # self.storage=new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
