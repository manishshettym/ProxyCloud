# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
 
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
 
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
 
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")


""" NOTE : threading.Thread(arg1 , arg2) -> this is using the constructor of the threading class to create 
an object called Thread -> if confused think of it as just a simple structure and an instance of that structure

As per what i read from the documentation file the arguments we will use are:

name => name of the thread so that it can be uniquely identified
target => target of the thread so that it can run thatt function in the seperate  thread
args => arguments for that function

SIMPLE ain't it ?? ;) 


The threading class now contains other methods like start() and join().

SO : 
Once the threads start, the current program (you can think of it like a main thread) also keeps on executing.
In order to stop execution of current program until a thread is complete, we use join method.
t1.join()
t2.join()
As a result, the current program will first wait for the completion of t1 and then t2.
Once, they are finished, the remaining statements of current program are executed.

 """