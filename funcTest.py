

def conflictCheckOne(index, func):
    func(index)
    return 10 



def conflictCheckTwo(index, func):
    func(index)
    print("안녕하세요")
    print("what are you doing")
    return 10 


def conflictCheckThree(index, func):
    func(index)
    print("conflict")
    return 10 


def conflictCheckFour(index):
    print("???")



