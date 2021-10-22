
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
        print('{} {}'.format(self.name, self.lname))
    
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
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)        

'''
# Here the apply raise method is applied
emp_1.apply_raise()
emp_2.apply_raise()
print('The total number of employees are {}'.format(Employee.number_of_employees))
'''

emp_str_1 = 'John-Doe-50000' 
emp_str_2 = 'Mark-Cuban-330000' 
emp_str_3 = 'Jack-Sterling-10000' 
emp_str_4 = 'Javier-Rodriguez-440000' 

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)
new_emp_4 = Employee.from_string(emp_str_4)

new_emp_1.fullname()
print(new_emp_1.email)
new_emp_2.fullname()
new_emp_3.fullname()
new_emp_4.fullname()


import datetime
my_date = datetime.date(2020, 8, 11)
print(Employee.check_workday(my_date))