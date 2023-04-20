

def checkOne(index, func, simple):
    print("helllo")
    
def checkFive(index, func):
    print("oh my good")
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