def hashFunc(value):
    sum = 0
    for char in value:
        sum += ord(char)
    return sum % 10

def addToList(key):
    index = hashFunc(key)
    bucketList[index].append(key)

def contains(key):
  index = hashFunc(key)
  return bucketList[index] == key

bucketList = [None, None, None, None, None, None, None, None, None, None]

addToList("test") 
print(bucketList)