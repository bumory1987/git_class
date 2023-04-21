def conflictOne(simple, value ,test):
    print(value(simple(test)))
    
def conflictTwo(simple, value ):
    def sol(simple,value ):
        simple(value)    
        return 10 
    value = sol(simple, value)
    
    
def conflictFour(index, func):
    solution=func(index)
    conflictTwo(func, solution)
    print("oh lord")
    
    
