def conflictOne(simple, value ,test):
    print("hello")
    
def conflictTwo(simple, value ):
    print("good job")   
    
def conflictThree(index, func):
    def sol(func,index ):
        func(index)    
        return 10 
    value = sol(index, func)
    print(value+10)
    
    
