try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Type a number")

# I can do one exception for everthing, like in the following example, but is a bad practice
try:
    number = int(input("Enter a number: "))
    print(1/number)
except Exception:
    print("Something went wrong") # We don't what is the error

# But we can combine those two ways

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Type a number")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")