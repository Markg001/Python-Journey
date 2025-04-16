def printExceptionsTree(ExceptionClass, level=0):
    if level > 1:
        print(" |" * (level - 1), end="")
    if level > 0:
        print(" +---", end="")
    print(ExceptionClass.__name__)
    
    for subclass in ExceptionClass.__subclasses__():
        printExceptionsTree(subclass, level + 1)

# Call the function with BaseException to print the hierarchy
printExceptionsTree(BaseException)
