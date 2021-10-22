# creating a class named programmers

class Employee:
    company = 'Microsoft' # the company attribute is a class attirbute because every programmers is from microsoft
    number_of_employees = 0

    def __init__(self, name, age, salary, job_role):    # This is a constructor
        self.name = name                                # These are instance attributes as "self" is given. This will refer to the object.
        self.age = age
        self.salary = salary
        self.job_role = job_role

        Employee.number_of_employees += 1

    
    def giveProgrammerInfo(self):
        print(f'\nThe name of the programmer is {self.name}')
        print(f'The age of the programmer is {self.age}')
        print(f'The salary of the programmer is {self.salary}')
        print(f'The job role of the programmer is {self.job_role}')
        print(f'The company of the programmer is {self.company} ')

# Here objects are created using the Employee class
ameya = Employee('Ameya', 22, 200000, 'Manager - Data Scientist')              
akshay = Employee('Akshay', 32, 100000, 'Senior Business Analyst')
prathamesh = Employee('Prathamesh', 25, 50000, 'Solution Architect')
nilesh = Employee('Nilesh', 30, 10000, 'Database Architect')
# here the class method is called by the objects
ameya.giveProgrammerInfo()
akshay.giveProgrammerInfo()
prathamesh.giveProgrammerInfo()


print(Employee.number_of_employees)


