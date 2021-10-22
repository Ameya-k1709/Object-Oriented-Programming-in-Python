# creating a class named calculator

class Calculator:
    # defining the init constructor
    def __init__(self, number):         # taking the input from the object using class and constructor
        self.number = number            # Giving the value of the instance attribute
                                        # here no class attribute is required

    # Defining the class method to perform the operations given in the question
    def performCalculation(self):
        print(f'\nThe square of the given number is {self.number**2}')          # Assigning the self keyword so that it refers to the object
        print(f'The cube of the given number is {self.number**3}')
        print(f'The square root of the given number is {self.number**0.5}\n')

# objects creation using class and constructor
number_1 = Calculator(2)
number_2 = Calculator(5)
number_3 = Calculator(7)
number_4 = Calculator(64)
number_5 = Calculator(16)

# applying class method to the objects that are created to perform the task.
number_1.performCalculation()
number_2.performCalculation()
number_3.performCalculation()
number_4.performCalculation()
number_5.performCalculation()
