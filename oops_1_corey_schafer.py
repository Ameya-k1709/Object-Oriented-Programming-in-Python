
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


emp_1 = Employee('Ameya', 'Kulkarni', 500000)
emp_2 = Employee('Prathamesh', 'Banait', 100000)

print(emp_1.email)
emp_1.fullname()
emp_1.apply_raise()
print('The total number of employees are {}'.format(Employee.number_of_employees))