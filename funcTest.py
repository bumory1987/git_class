

def conflictCheckOne(index, functt):
    functt(index)
    return 10 



def conflictCheckTwo(index, func):
    return func(index)


def conflictCheckThree(index, func):
    func(index)
    print("no more")
    print("conflict")
    return 10 


def conflictCheckFour(index):
    print("conflict start")
    print("show me")


def conflictCheckFour(index, func):
    func(index)
    print("other conflict")
    return 10 


