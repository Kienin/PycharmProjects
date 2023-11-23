# EXCEPTIONS = events detected during execution that interrupt the flow of a program

# Simple division calculator:

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Eneter a number to divide by: "))
    quotient = numerator / denominator
except ZeroDivisionError as e:                                            # Good practice to catch specific exceptions
    print(e)                                                              # as e: prints out what the problem is
    print("You can't divide by zero...")
except ValueError as e:
    print(e)
    print("Enter only numbers please.")
except Exception as e:                                                    # except Exception: should be the very last exception
    print(e)
    print("Something went wrong")
else:
    print(quotient)
finally:                                                                  # finally: will always execute regardless of exception
    print("This will always execute")

print("--------------------------------")
