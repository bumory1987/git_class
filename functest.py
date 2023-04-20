

def checkOne(index, funct):
    print("helllo")
    
def checkTwo(index, func):
    return func(index)

def checkThree(index, func):
    def funcAdd(index):
        return index+1 
    result = funcAdd(index)
    print(result)