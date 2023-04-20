

def conflictCheckOne(index, func):
    func(index)
    return 10 



def conflictCheckTwo(index, func):
    print("no no no ")
    print("on my god")


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


