class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""
    def __init__(self, message="Value is too small!"):
        self.message = message
        super().__init__(self.message)

class ValueTooLargeError(CustomError):
    """Raised when the input value is too large"""
    def __init__(self, message="Value is too large!"):
        self.message = message
        super().__init__(self.message)

def check_value(value):
    if value < 10:
        raise ValueTooSmallError()
    elif value > 20:
        raise ValueTooLargeError()
    else:
        print("Value is within the acceptable range.")

# Test the custom exceptions
try:
    check_value(5)
except ValueTooSmallError as e:
    print(e)


# try:
#     check_value(25)
# except ValueTooSmallError as e:
#     print(e)
# except ValueTooLargeError as e:
#     print(e)
#
# try:
#     check_value(15)
# except CustomError as e:
#     print(e)
