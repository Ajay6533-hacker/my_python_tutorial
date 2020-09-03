                                    # Local variable , global variable and global keyword
"""                                    
k=10           # global variable
def func():
    a=36         # local variabel
    #k=36        # local variable
    global k          # after built of global keyword we can change the value in inside the function
    k=k+10
    c=a+k
    print(c)
func()"""

def ajay():
    a=45
    def vijay():
        s=45
        global a
        a=37
        print(a)
    vijay()
ajay()
