
# print("Welcome to India")

# print(x)

# print("Thank you")

# ================== Exception Handling ==================

"""
    try
    except
    else
    finally


    try:

        The block where you write the code that might raise an exception.
        Python attempts to execute this block first.
        If an error occurs, the control is transferred to the except block.

    except:

        The block where you handle the error or exception.
        You can specify the type of exception to handle specific errors.
        If no error occurs, this block is skipped.

    else:

        Executes if the code in the try block runs successfully without raising any exception.

    finally:

        This block always executes, regardless of whether an exception was raised or not.
        Useful for cleanup operations like closing files or database connections.


    
    Syntax :


        try:
        
            # test a block of code for errors

        except :
            
            # handle the error

        else:

            # code to be executed if no error occurs

        finally :

            execute code, regardless of the outcome

"""
# print(x)
"""
try :
    print(x)

except NameError as e:

    print("An Error Occurred",e)

else:
    print("No Error Occurred")

finally:
    print("Execution Completed")

    """
# ======================

"""
try:

    x = 10/"hello"
    print(x)

except ZeroDivisionError as e:
    print("Division by zero error occurred:", e)

except Exception as e:
    print("An Error Occurred", e)

"""

# Creating Custom Exception :

"""
class NegativeNumberError(Exception):
    pass

# Custom Exception Handling Example

try:

    num = int(input("Enter a Positive Number : "))

    if num < 0:

        raise NegativeNumberError("Negative numbers are not allowed")
    
except NegativeNumberError as e:
    print("Custom Exception Occurred:", e)

else:
    print("Numbers --> ",num)

finally:
    print("Execution Completed")

"""

# Built-ins in Python :

errors = dir(locals()['__builtins__'])

print(len(errors))

print(errors)


