

def checkOne(index, func):
    print("helllo")
    
def checkTwo(index, func):
    print("hello")
    return func(index)

def checkThree(index, func):
    def funcFianl(index):
        fIndex = index * index
        return fIndex
    def funcADD(index):
        fIndex = index + index
        return fIndex
    result = funcADD(funcFianl(index))
    return result