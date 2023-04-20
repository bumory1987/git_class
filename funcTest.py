

def conflictCheckOne(index, func):
    func(index)
    return 10 



def conflictCheckTwo(index, func):
    print("check point")
    print("안녕하세요")
    return 10 


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


