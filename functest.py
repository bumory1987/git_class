

def checkOne(index, func, simple):
    val=simple(index)
    print("helllo + {val}")
    
def checkFive(index, func):

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