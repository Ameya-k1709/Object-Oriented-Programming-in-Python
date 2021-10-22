
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)


    # Defining the fullname class method which takes an instance self (i.e the object/instance)

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

emp1 = Employee('Rakesh', 'Om')

# Changing the value of the instance attribute 'fname' to check if other attributes are also updated.
emp1.fname = 'Vilass'

print(emp1.fname)

# As we have changed the value of fname earlier, the email attribute also must adapt to the new updates
# But it isn't updated, it is holding the same old value. 
print(emp1.email)
print(emp1.fullname())