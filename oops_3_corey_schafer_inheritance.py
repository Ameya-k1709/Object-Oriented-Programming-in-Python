
class Employee:

    number_of_employees = 0
    raise_amount = 1.05

    def __init__(self, name, lname, salary):
        self.name = name
        self.lname = lname
        self.salary = salary
        self.email = name + '.' + lname + '@gmail.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.name, self.lname)
    
    def apply_raise(self):
        print('The amount after the applied raise is {}'.format(self.salary*Employee.raise_amount ))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def check_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print('This is a weekend')
        else:
            print('This is a workday')

emp_1 = Employee('Ameya', 'Kulkarni', 500000)
emp_2 = Employee('Prathamesh', 'Banait', 100000)

#print(emp_1.email)
#emp_1.fullname()

# Using the @classmenthod to set the raise_amount, this can also be done directly by changing the value of the class attribute.

Employee.set_raise_amount(1.08)

#Here the objects are also set to the updated raise_amount as it is a class attribute and not an instance attribute
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
#print(Employee.raise_amount)        

'''
# Here the apply raise method is applied
emp_1.apply_raise()
emp_2.apply_raise()
print('The total number of employees are {}'.format(Employee.number_of_employees))
'''

# Creating a developer sub-class which is inherited from the Employee class. Here all the Employee attributes are retained by the sub class with the super() method
class Developer(Employee):
    def __init__(self, name, lname, salary, prog_language):
        super().__init__(name, lname, salary)               # Here the super() method is used to inherit all the attributed of the __init__ method of the parent class.
        self.prog_language = prog_language


class Manager(Employee):
    def __init__(self, name, lname, salary, employee_managed=None):  # default argument is given None value, hence employee_managed is None
        super().__init__(name, lname, salary)
        if employee_managed is None:
            self.employee_managed = []
        else:
            self.employee_managed = employee_managed
        
    def add_manager(self, emp):
        if emp not in self.employee_managed:
            self.employee_managed.append(emp)

    def remove_manager(self, emp):
        if emp in self.employee_managed:
            self.employee_managed.remove(emp)

    def tot_managed(self):
        print("\nThe names of the employees managed by {} are:".format(self.name))
        for emp in self.employee_managed:
            print(" -->> ", emp.fullname())

# creating the Developer class
dev_1 = Developer('John', 'Do', 500000, 'Python')
dev_2 = Developer('Shang', 'Chi', 300000, 'Java')
dev_3 = Developer('Yang', 'Min', 400000, 'PHP')
dev_4 = Developer('Ruskin', 'Bond', 500000, 'C')
dev_5 = Developer('Mel', 'Robbins', 1100000, 'C++')


# Here we are printing the instance attribute prog_lang from the Developer
#print(dev_1.prog_language)
#print(dev_2.prog_language)

manager_1 = Manager('Justin', 'Ng', 100000, [dev_1])
manager_2 = Manager('Tony', 'Robbins', 300000, [dev_4])
manager_3 = Manager('Russell', 'Peters', 400000, [dev_2])
manager_4 = Manager('Jose', 'Rogan', 500000, [dev_3])

manager_1.add_manager(dev_2)
manager_1.add_manager(dev_3)
manager_1.add_manager(dev_5)
#print(manager_1.__dict__)
manager_1.tot_managed()

