x = 'hi'

try:
   # print(x/1)
    if not type(x) is str: # If x is not a string then raise a type error, this is caught in the 'except Exception' block
        raise TypeError("Only str allowed.")
    else: raise Exception("I'm a custom exception / error.")
except NameError:
    print('NameError - Something undefined.')
except ZeroDivisionError:
    print("ZeroDivisionError - Don't divide by zero.")
except Exception as error:
    print(error)
else: # This block is run if no errors are found.
    print('No Error!')
finally: # No matter if we have an error or not, we will always reach the finally block
    print("How's about that weather?")