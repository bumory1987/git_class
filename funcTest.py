

def conflictCheckOne(index, func):
    func(index)
    return 10 



def conflictCheckTwoThreeFour(index, func):
    print("no no no ")
    print("on my god")

def conflictCheckThree(index, func):
    print("conflict")
    return 10 


def conflictCheckFour(index, func):
    func(10)
    print("show me")

def conflictCheckFour(index, func):
    func(index)
    print("other conflict")
    return 10 


