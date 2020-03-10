import hashlib
n = 1
#bytearray give a string of just the bytes
key = b'my_value'
key2 = "string1".encode()
key3 = b'lunchtime'


# for i in range(n):
#     print(hash(key))
#     print(hashlib.sha256(key).hexdigest())

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8


print(index)
print(index2)
print(index3)


# for i in range(n):
#     print(hash(key))
# for i in range(n):
#     print(hash(key2))
