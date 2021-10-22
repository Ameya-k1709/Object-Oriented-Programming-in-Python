
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
     
    # Using the property decorator for using the email() method as an instance attribute, so that we don't have to change every occurance of the email attribute 
    @property
    # Here converting the email attribute which was declared in the __init__ method to an email() method so that it gets updated with changes in code,
    # which it was failing to do in the previous file when other attributes were updated.
    def email(self):
        return "{}.{}@gmail.com".format(self.fname, self.lname)

    # adding the property decorator to the fullname() method 
    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    # creating the setter for the fullname() method
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname

    # creating a deletor for the fullname() method
    @fullname.deleter
    def fullname(self):
        print("Deleted fullname!!!")
        self.fname = None
        self.lname = None

emp1 = Employee('Rakesh', 'Om')

emp1.fname = 'Vilass'

emp1.fullname = "Ameya Kulkarni"
print(emp1.fname)

# As we have changed the value of fname earlier, the email attribute also must adapt to the new updates
# But it isn't updated, it is holding the same old value. 
print(emp1.email)
print(emp1.fullname)

# del emp1.fullname

# print(emp1.fullname)
# print(emp1.fname, emp1.lname)
# print(emp1.lname)