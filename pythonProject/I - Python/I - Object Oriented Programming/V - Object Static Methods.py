# STATIC METHODS: bound to a class rather than the objects for that class.
# This means that a static method can be called without an object for that class.

class Math:

    # define methods that aren't specific to an instance:
    @staticmethod            # @staticmethod is unchanging
    def add5(x):
        return x + 5

    @staticmethod  # @staticmethod is unchanging
    def subtract5(x):
        return x - 5

    @staticmethod  # @staticmethod is unchanging
    def multiply5(x):
        return x * 5

    @staticmethod  # @staticmethod is unchanging
    def divide5(x):
        return x / 5

    @staticmethod
    def pr():
        print("Hello World")

print(Math.add5(5))
Math.pr()