

def conflictCheckOne(index, func):
    func(index)
    return 10 



def conflictCheckTwo(index, func):
    def showConflict(index):
        return index + 1 
    func(showConflict(index))


def conflictCheckThree(index, func):
    func(index)
    print("conflict")
    return 10 


def conflictCheckFour(index):
    print("show me")

def conflictCheckFour(index, func):
    func(index)
    print("conflict")
    return 10 


