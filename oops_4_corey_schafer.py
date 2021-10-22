
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

    # Employee('Name','lname', salary)
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.name, self.lname, self.salary)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        print("\nThe number of characters in the Employee named {} are: ".format(self.name), end='') 
        return len(self.fullname())


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

emp_1 = Employee('Ameya', 'Kulkarni', 500000)
emp_2 = Employee('Prathamesh', 'Banait', 100000)

# print(emp_1.email)
# emp_1.fullname()
# emp_1.apply_raise()
# print('The total number of employees are {}'.format(Employee.number_of_employees))

print( "\nThe sum of employee salaries is", emp_1 + emp_2, sep=" -->> ", end='')
print(len(emp_2))