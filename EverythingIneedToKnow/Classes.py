# ----------------------------------------------------------
#  Understanding Classes and Constructors in Python GOd I miss my OOP class 
# ----------------------------------------------------------

# A class is like a blueprint for creating objects.
# It bundles data (variables) and behavior (functions) together.
# ----------------------------------------------------------

class MyClass:
    # ------------------------------------------------------
    # 🔹 Constructor (__init__)
    # The constructor is automatically called when
    # you create an instance of the class.
    # It initializes the object with values you pass in.
    # ------------------------------------------------------
    def __init__(self, nums):
        # Create member variables (attributes)
        self.nums = nums              # store the list passed in
        self.size = len(nums)         # store the length of the list

    # ------------------------------------------------------
    # 🔹 Instance Method
    # Every method inside a class must have 'self' as the first parameter.
    # 'self' refers to the current object (instance) of the class.
    # ------------------------------------------------------
    def getLength(self):
        # Access the 'size' attribute of the current object
        return self.size

    # ------------------------------------------------------
    # 🔹 Another Instance Method
    # Methods in the same class can call each other using 'self'.
    # ------------------------------------------------------
    def getDoubleLength(self):
        # Calls getLength() and multiplies it by 2
        return 2 * self.getLength()


# ----------------------------------------------------------
# 🧩 Using the Class
# ----------------------------------------------------------

# Create an object (instance) of MyClass
nums = [10, 20, 30, 40]
obj = MyClass(nums)   # calls __init__ automatically

# Access methods using the dot (.) operator
print("Numbers:", obj.nums)                     # [10, 20, 30, 40]
print("Length of list:", obj.getLength())       # 4
print("Double of length:", obj.getDoubleLength())  # 8

# ----------------------------------------------------------
# 💡 Summary:
# - 'class' defines a blueprint for objects.
# - '__init__' is the constructor (sets up data for each object).
# - 'self' refers to the current object.
# - You can access attributes and methods using 'self'.
# ----------------------------------------------------------
