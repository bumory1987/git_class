def conflictOne(simple, value ,test):
    print("hello")
    
def conflictTwo(simple, value ):
    total=simple(value)*4
    print(total)
    
def conflictThree(index, func):
    def sol(func,index ):
        func(index)    
        return 10 
    value = sol(index, func)
    print(value+10)
    
    
